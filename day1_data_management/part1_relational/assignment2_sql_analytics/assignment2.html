<html>

<head>

<title>Assignment 2 - Databases and Basic Text Analytics</title>

<style>
.turnin {
color:red;
font-size:120%;
}
.important {
color:purple;
}
p {
padding-bottom:0.25em;
}
h3 {
padding-top:2em;
}
h4 {
padding-top:1em;
}
</style>

</head>

In the virtual machine, please open a Terminal to complete this assignment. Some  
relevant commands and notes for this assignment:
<ul>
<li><code>cd directory_name</code> : change directory to <code>directory_name</code></li>
<li><code>ls</code> : list files in the current directory </li>
<li><code>sqlite3 reuters.db &lt; sql_filename</code> : execute the queries in the file <code>sql_filename</code>against the database <code>reuters.db</code>.  This command assumes <code>reuters.db</code> and <code>sql_filename</code> are in your current directory.</li>
<li> Pressing the tab key will attempt to autocomplete any command or filename you are currently typing.</li>
<li> For Problem 2, you will use matrix.db instead of reuters.db</li>
</ul>

<p>
Before you start the assignment, please go to the git repository and get the most recent course materials by issuing the following command: <strong>git pull</strong>
</p>

<p>For most of these problems, you will use the <a href="https://github.com/uwescience/datasci_course_materials">reuters.db</a> database consisting of a single table:</p>

<pre>frequency(docid, term, count)</pre>
<p>
where <code>docid</code> is a document identifier corresponding to a particular file of text, <code>term</code> is an English word, and <code>count</code> is the number of the occurrences of the term within the document indicated by <code>docid</code>.
</p>
<p>
Many questions ask you to count the number of records returned by a query. Perhaps the easiest way to count the number of records returned by a query Q is to write Q as a subquery:
</p>

<pre>
SELECT count(*) FROM (
  SELECT ...

) x;
</pre>
<p>
(In SQLite, the alias "x" is not required, but in other dialects of SQL it is. So we've included it here.)
</p>


<h3>Problem 1: Inspecting the Reuters Dataset; Basic Relational Algebra</h3>

<p><strong>(a) select:</strong> Write a query that is equivalent to the following
relational algebra expression.</p>

<p>
&sigma;<sub>docid=10398_txt_earn</sub>(frequency)
</p>

<p class="turnin">What to turn in: Run your query against your local database and determine the number of records returned. Save that value in a .txt file . You can name the file anything. On the assignment page, upload the file as your answer.
</p>


<p>
<strong>(b) select project:</strong> Write a SQL statement that is equivalent to the following relational algebra expression.
</p>

<p>
&pi;<sub>term</sub>(&sigma;<sub>docid=10398_txt_earn and count=1</sub>(frequency))
</p>

<p class="turnin">What to turn in: Run your query against your local database and determine the number of records returned. Save that value in a .txt file . You can name the file anything. On the assignment page, upload the file as your answer.</p>

<p><strong>(c) union:</strong> Write a SQL statement that is equivalent to the following relational algebra expression. (Hint: you can use the UNION keyword in SQL)</p> 

<p>
&pi;<sub>term</sub>(&sigma;<sub>docid=10398_txt_earn and count=1</sub>(frequency)) U &pi;<sub>term</sub>(&sigma;<sub>docid=925_txt_trade and count=1</sub>(frequency))
</p>

<p class="turnin">What to turn in: Run your query against your local database and determine the number of records returned. Save that value in a .txt file . You can name the file anything. On the assignment page, upload the file as your answer.</p>

<p><strong>(d) count:</strong> Write a SQL statement to count the number of documents
containing the word "parliament"</p>

<p class="turnin">What to turn in: Run your query against your local database and determine the number of records returned. Save that value in a .txt file . You can name the file anything. On the assignment page, upload the file as your answer.</p>

<p><strong>(e) big documents</strong> Write a SQL statement to find all documents that have
more than 300 total terms, including duplicate terms.  (Hint: You can use the HAVING clause, or you can use a nested query.  Another hint: Remember that the count column contains the term frequencies, and you want to consider duplicates.) (docid, term_count)
</p>

<p class="turnin">What to turn in: Run your query against your local database and determine the number of records returned. Save that value in a .txt file . You can name the file anything. On the assignment page, upload the file as your answer.</p>


<p><strong>(f) two words:</strong> Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'. </p>

<p class="turnin">What to turn in: Run your query against your local database and determine the number of records returned as described above.  On the assignment page, turn in a text file <code>two_words.txt</code> that contains the number of records.</p>


<h3>Problem 2: Matrix Multiplication in SQL</h3>

<p>
Recall from lecture that a sparse matrix has many positions with a value of zero. 
</p>

<p>
Systems designed to efficiently support sparse matrices look a lot like databases: They represent each cell as a record <code>(i,j,value)</code>. 
</p>

<p>
The benefit is that you only need one record for every non-zero element of a matrix.
</p>
<p>
For example, the matrix
</p>



<table>
 <tr>
  <td>0</td><td>2</td><td>-1</td>
 </tr>
 <tr>
  <td>1</td><td>0</td><td>0</td>
 </tr>
 <tr>
  <td>0</td><td>0</td><td>-3</td>
 </tr>
  <tr>
  <td>0</td><td>0</td><td>0</td>
 </tr>
 </table>


<p>can be represented as a table</p>


<TABLE border="1" cellpadding="3" cellspacing="0" width="300">
<tr>
<td width="50%" align="center">
row #
</td>
<td width="50%" align="center">
column #
</td>
<td width="50%" align="center">
value
</td>
</tr>
<tr>
<td width="33%" align="center">
0
</td>
<td width="50%" align="center">
1
</td>
<td width="50%" align="center">
2
</td>
</tr>
<tr>
<td width="33%" align="center">
0
</td>
<td width="50%" align="center">
2
</td>
<td width="50%" align="center">
-1
</td>
</tr>
<tr>
<td width="33%" align="center">
1
</td>
<td width="50%" align="center">
0
</td>
<td width="50%" align="center">
1
</td>
</tr>
<tr>
<td width="33%" align="center">
2
</td>
<td width="50%" align="center">
2
</td>
<td width="50%" align="center">
-3
</td>
</tr>
</TABLE>


<p>Take a minute to make sure you understand how to convert back and forth between these two representations.</p>

<p>Now, since you can represent a sparse matrix as a table, it's reasonable to consider whether you can express matrix multiplication as a SQL query and whether it makes sense to do so.</p>

<p>
Within <a href="https://github.com/uwescience/datasci_course_materials/blob/master/assignment2/matrix.db">matrix.db</a>, there are two matrices A and B represented as follows:
</p>
<pre>
A(row_num, col_num, value)

B(row_num, col_num, value)
</pre>
<p>
The matrix A and matrix B are both square matrices with 5 rows and 5 columns each.
</p>


<p><strong>(g) multiply:</strong> Express A X B as a SQL query, referring to the
class lecture for hints.</p>


<p class="turnin">What to turn in: Save the value of cell (2,3) in a .txt file. You can name the file anything you like. On the assignment page, upload the file contatining only the value of the cell (2,3)</p>

If you're wondering why this might be a good idea, consider that advanced databases execute queries in parallel automatically.   So it can be quite efficient to process a very large sparse matrix --- millions of rows or columns --- in a database.

But a word of warning: In a job interview, don't tell them you recommend implementing linear algebra in a database.  You won't be wrong, but they won't understand databases as well as you now do, and therefore won't understand when and why this is a good idea.   Just say you have done some experiments using databases for analytics, then mention the papers in the reading if they seem incredulous!

<h3>Problem 3: Working with a Term-Document Matrix</h3>

<p>The reuters dataset can be considered a <em>term-document matrix</em>, which is an important representation for text analytics.</p>

<p>
The reuters dataset can be considered a <em>term-document matrix</em>, which is an important representation for text analytics.
</p>
<p>
Each row of the matrix is a <em>document vector</em>, with one column for every term in the entire corpus.  Naturally, some documents may not contain a given term, so this matrix is rather sparse. The value in each cell of the matrix is the term frequency.  (You'd often want this this value to be a <em>weighted</em> term frequency, typically using &quot;tf-idf&quot;: <em>term frequency - inverse document frequency</em>. But we'll stick with the raw frequency for now.)
</p>
<p>
What can you do with the term-document matrix <em>D</em>? One thing you can do is compute the similarity of documents. Just multiply the matrix with its own transpose <em>S = DD<sup>T</sup></em>, and you have an (unnormalized) measure of similarity.
</p>

<p>
The result is a square document-document matrix, where each cell represents the similarity. Here, similarity is pretty simple: if two documents both contain a term, then the score goes up by the product of the two term frequencies. This score is equivalent to the dot product of the two document vectors.
</p>

<p>To normalize this score to the range 0-1 and to account for relative term frequencies, the <em>cosine similarity</em> is perhaps more useful.  The cosine similarity is a measure of the angle between the two document vectors, normalized by magnitude.  You just divide the dot product by the magnitude of the two vectors.  However, we would need a power function (x^2, x^(1/2)) to compute the magnitude, and sqlite has <a href="http://www.sqlite.org/lang_corefunc.html">built-in support for only very basic mathematical functions<a/>.  It is not hard to <a href="https://www.google.com/search?q=math+function+extensions+sqlite">extend sqlite to add what you need</a>, but we won't be doing that in this assignment.
</p>

<p><strong>(h) similarity matrix:</strong> Write a query to compute the similarity matrix <em>DD<sup>T</sup></em>. (Hint: The transpose is trivial -- just join on columns to columns instead of columns to rows.)  The query could take some time to run if you compute the entire result.  But notice that you don't need to compute the similarity of both (doc1, doc2) and (doc2, doc1) -- they are the same, since similarity is symmetric.  If you wish, you can avoid this wasted work by adding a condition of the form a.docid &lt; b.docid to your query.  (But the query still won't return immediately if you try to compute every result -- don't expect otherwise.)</p>

<p class="turnin">What to turn in: On the assignment page, enter a .txt file containing the similarity value of the two documents '10080_txt_crude' and '17035_txt_earn'. You can name the file anything you like.</p>

<p>You can also use this similarity metric to implement some primitive search capabilities.  Consider a keyword query that you might type into Google: It's a bag of words, just like a document (typically a keyword query will have far fewer terms than a document, but that's ok).</p>

<p>So if we can compute the similarity of two documents, we can compute the similarity of a query with a document.  You can imagine taking the union of the keywords represented as a small set of (docid, term, count) tuples with the set of all documents in the corpus, then recomputing the similarity matrix and returning the top 10 highest scoring documents.
</p>

<p><strong>(i) keyword search:</strong> Find the best matching document to the keyword query "washington taxes treasury".  You can add this set of keywords to the document corpus with a union of scalar queries: 
<pre>
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
</pre>

Then, compute the similarity matrix again, but filter for only similarities involving the "query document": docid = 'q'.  Consider creating a view of this new corpus to simplify things.
</p>

<p class="turnin">What to turn in: On the assignment page, enter the maximum similarity score between the keyword query and any document.  Your SQL query should return a list of (docid, similarity) pairs, but you will submit only a single number: the highest score in the list.</span></p>


</div>

</body>

</html>