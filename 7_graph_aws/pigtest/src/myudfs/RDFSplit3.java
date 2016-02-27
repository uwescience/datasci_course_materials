package myudfs;

import java.io.IOException;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.PatternSyntaxException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.lang.IllegalStateException;

import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;
import org.apache.pig.data.TupleFactory;

public class RDFSplit3 extends EvalFunc<Tuple> {
    private final static TupleFactory tupleFactory = TupleFactory.getInstance();
    private final static NQuadParser nquadParser = new NQuadParser();

    public Tuple exec(Tuple input) throws IOException {
        if (input == null || input.size() < 1)
            return null;
        try {
            String source = (String) input.get(0);
            if (source == null) {
                return null;
            }

            ArrayList<String> result = new ArrayList<String>(3);
            if ( nquadParser.parse(source,result) ) {
				return tupleFactory.newTupleNoCopy(result);
			} else {
            }
            return null;
        } catch (Exception e) {
			log.warn("offending string: "+input.get(0));
            log.error(e);
		}	
        // this only happens if the try block did not complete normally
        return null;
    }
}
