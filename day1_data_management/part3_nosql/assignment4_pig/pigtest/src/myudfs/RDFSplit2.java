/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package myudfs;

import java.io.IOException;

import java.util.ArrayList;
import java.util.regex.PatternSyntaxException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.lang.IllegalStateException;

import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;
import org.apache.pig.data.TupleFactory;

/**
 * Wrapper around Java's String.split<br>
 * input tuple: first column is assumed to have a string to split;<br>
 * the optional second column is assumed to have the delimiter or regex to split on;<br>
 * if not provided, it's assumed to be '\s' (space)<br>
 * the optional third column may provide a limit to the number of results.<br>
 * If limit is not provided, 0 is assumed, as per Java's split().
 */

/**
 * @deprecated Use {@link org.apache.pig.builtin.STRSPLIT}
 */

public class RDFSplit2 extends EvalFunc<Tuple> {

    private final static TupleFactory tupleFactory = TupleFactory.getInstance();
	
	private static String uriRef = "(<.*>)";
	private static String languageString = "(\".*\""+"(@"+"[a-z]+(-[a-z0-9]+)*)?)";
	private static String dataTypeString = "(\".*\""+"\\^\\^"+"<.*>)";
	private static String nodeID = "(_:[a-zA-Z][_a-zA-Z0-9]*)";
	private static String literal = "("+languageString+"|"+dataTypeString+")";
	
	private static String subject ="("+uriRef+"|"+nodeID+")"; //will be group 1
	private static String predicate = uriRef; //will be group 4
	private static String object = "("+uriRef+"|"+nodeID+"|"+literal+")";//will be group 5
	private static String context = uriRef; //will be group 10


    private static String NQuadPatternString = "^\\s*"+subject+"\\s+"+predicate+"\\s+"+object+"\\s+"+context+"\\s+"+"\\."+"\\s*";
    
    private static Pattern NQuadPattern = Pattern.compile(NQuadPatternString);

    /**
     * Parser to get RDF data
     * @param input tuple; first column is assumed to have a string to split;
     * the optional second column is assumed to have the delimiter or regex to split on;<br>
     * if not provided, it's assumed to be '\s' (space)
     * the optional third column may provide a limit to the number of results.<br>
     * If limit is not provided, 0 is assumed, as per Java's split().
     * @exception java.io.IOException
     */
    public Tuple exec(Tuple input) throws IOException {
        if (input == null || input.size() < 1)
            return null;
        try {
            String source = (String) input.get(0);
            if (source == null) {
                return null;
            }
			
			// hopefully this will be the correct pattern for parsing n-quads
			//String NQuadPatternString = "^\\s*"+subject+"\\s+"+predicate+"\\s+"+object+"\\s+"+context+"\\s+"+"\\."+"\\s*";
			//log.warn(NQuadPatternString);
			//log.warn(source);
			//Pattern NQuadPattern = Pattern.compile(NQuadPatternString);
			Matcher NQuadMatcher = NQuadPattern.matcher(source);
			boolean matched_source = NQuadMatcher.matches();
			// I've updated the strings so hopefully we won't get junk tuples anymore, but just in case
			if(!matched_source) {
				log.warn("did not fully match the source: "+source);
				ArrayList<String> junk = new ArrayList<String>(3);
				junk.add("junk");
				junk.add("junk");
				junk.add("junk");
				return tupleFactory.newTupleNoCopy(junk);
			} else {
				// not sure if the Matcher always returns an object, so I just check for null anyway
				String parsedSubject = (NQuadMatcher.group(1) != null) ? NQuadMatcher.group(1) : "";
				String parsedPredicate = (NQuadMatcher.group(4) != null) ? NQuadMatcher.group(4) : "";
				String parsedObject = (NQuadMatcher.group(5) != null) ? NQuadMatcher.group(5) : "";
				
				ArrayList<String> NQuad = new ArrayList<String>(3);
				NQuad.add(parsedSubject);
				NQuad.add(parsedPredicate);
				NQuad.add(parsedObject);
				
				return tupleFactory.newTupleNoCopy(NQuad);
			}
			
			
        } catch (ClassCastException e) {
            log.warn("class cast exception at "+e.getStackTrace()[0]);
        } catch (PatternSyntaxException e) {
            log.warn(e.getMessage());
        } catch (IllegalStateException e) { // shouldn't get here anymore, but just in case
			log.warn("illegal state exception at "+e.getStackTrace()[0]);
			log.warn("offending string: "+input.get(0));
		}	
        // this only happens if the try block did not complete normally
        return null;
    }
}
