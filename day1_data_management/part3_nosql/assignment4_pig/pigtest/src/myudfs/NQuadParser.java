package myudfs;
// Code from YongChul for CSE344 project. Modified to make it work on context.

import java.io.IOException;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.PatternSyntaxException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.lang.IllegalStateException;


public final class NQuadParser {
	int pos;
	String l; // current processing line

	private boolean skipWhiteSpace() {
		if ( pos < 0 ) return false;
		for ( ; pos < l.length(); ++pos ) {
			char ch = l.charAt(pos);
			if ( ch != ' ' && ch != '\t' ) break;
		}
		return pos < l.length();
	}

	private int skipNonWhiteSpaceOrUri(int i) {
		char ch;
		for ( ; i < l.length(); ++i ) {
			ch = l.charAt(i);
			if ( ch == ' ' || ch == '\t' ) {
				break;
			} else {
				int end = -1;
				if ( ch == '<' ) {
					// look for matching '>'
					end = l.indexOf('>',i);
					if ( end >= 0 ) {
						++end;
						return end;
					}
				} else if ( ch == '_') {
					// look for the first white space
					end = skipNonWhiteSpace(i+1);
					return end;
				} 
			}
		}
		return i;
	}
	
	private int skipNonWhiteSpace(int i) {
		char ch;
		for ( ; i < l.length(); ++i ) {
			ch = l.charAt(i);
			if ( ch == ' ' || ch == '\t' ) break;
		}
		return i;
	}

	private String extractSubject() {
		char ch = l.charAt(pos);
		int end = -1;
		if ( ch == '<' ) {
			// look for matching '>'
			end = l.indexOf('>',pos);
			if ( end >= 0 ) {
				++end;
			}
		} else if ( ch == '_') {
			// look for the first white space
			end = skipNonWhiteSpace(pos+1);
		} else {
			// screwed!
			pos = -1;
			return null;
		}
		int pos2 = pos;
		if ( end >= 0 ) {
			pos = end;
		} else {
			pos = -1;
		}
		return ( end < 0 ) ? null : l.substring(pos2, end);
	}

	private String extractPredicate() {
		if ( pos < 0 ) return null;

		char ch = l.charAt(pos);
		int end = -1;
		if ( ch == '<' ) {
			// look for matching '>'
			end = l.indexOf('>',pos);
			if ( end >= 0 ) {
				++end;
			}
		} else {
			// screwed!
			pos = -1;
			return null;
		}
		int pos2 = pos;
		if ( end >= 0 ) {
			pos = end;
		} else {
			pos = -1;
		}
		return ( end < 0 ) ? null : l.substring(pos2, end);
	}
	
	private int countPrecedingSlashes(String l, int pos) {
		int posOffset = 1;
		int count = 0;
		while( ((pos-posOffset) > 0) && (l.charAt(pos-posOffset) == '\\') ) {
			count = count + 1;
			posOffset = posOffset+1;
		}
		return count;
	}

	private String extractObject() {
		if ( pos < 0 ) return null;

		char ch = l.charAt(pos);
		int end = -1;
		if ( ch == '<' ) {
			// look for matching '>'
			end = l.indexOf('>',pos);
			if ( end >= 0 ) {
				++end;
			}
		} else if ( ch == '_') {
			// look for the first white space
			end = skipNonWhiteSpace(pos+1);
		} else if ( ch == '"' ) {
			// look for another quote
			int newEnd = pos+1; //end;
			
			while ( newEnd < l.length() ) {
				int xxx = l.indexOf('"',newEnd);
				int precedingSlashes = countPrecedingSlashes(l, xxx);
				// check whether it is escaped
				if ( xxx < 0 ) {
					pos = -1;
					return null;
				//} else if ( l.charAt(xxx-1) != '\\' || ( l.charAt(xxx-1) == '\\' && l.charAt(xxx-2) == '\\')) {
				} else if( (precedingSlashes % 2) == 0) {
					// we got it right.
					end = xxx;
					break;
				}
				newEnd = xxx+1;
			}

			// sanity check
			if ( l.charAt(end) != '"' ) {
				pos = -1;
				return null;
			}

			// now skip all non-white spaces
			//end = skipNonWhiteSpace(end);
			end = skipNonWhiteSpaceOrUri(end);
		} else {
			// screwed!
			pos = -1;
			return null;
		}

		int pos2 = pos;
		if ( end >= 0 ) {
			pos = end;
		} else {
			pos = -1;
		}
		return ( end < 0 ) ? null : l.substring(pos2, end);	
	}

	private void debug(String s, List<String> res) {
		if( pos < 0 ) {
			System.err.println("YIKES! Position 0! for s: "+s);
			for(int i = 0; i < res.size(); i=i+1 ) {
				String r = (String)res.get(i);
				System.err.println("["+i+"]: "+r);
			}
		}
	}
	
	public boolean parse(String s,List<String> res) {
		l = s;
		pos = 0;
		skipWhiteSpace(); // remove leading white space
		debug(s,res);
		String subject = this.extractSubject();
		skipWhiteSpace();
		debug(s,res);
		String predicate = this.extractPredicate();
		skipWhiteSpace();
		debug(s,res);
		String object = this.extractObject();
		skipWhiteSpace();
		debug(s,res);
		String context = this.extractSubject();

		res.add(subject);
		res.add(predicate);
		res.add(object);
		res.add(context);
		
		if( subject == null ) {
			System.err.println("s: "+s);
			System.err.println("subject: null");
		//} else {
		//	System.err.println("subject: "+subject);
		}
		if( predicate == null ) {
			System.err.println("s: "+s);
			System.err.println("predicate: null");
		//} else {
		//	System.err.println("predicate: "+predicate);
		}
		if( object == null ) {
			System.err.println("s: "+s);
			System.err.println("object: null");
		//} else {
		//	System.err.println("object: "+object);
		}
		if( context == null ) {
			System.err.println("s: "+s);
			System.err.println("context: null");
		//} else {
		//	System.err.println("context: "+context);
		}

		return subject != null && object != null && predicate != null && context != null;
	}
}

