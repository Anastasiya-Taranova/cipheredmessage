# Ciphered message
<h2><a id="user-content-installation" class="anchor" aria-hidden="true" href="#installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>RUN</h2>
<code> python edward.py <somefile.txt> </code><br>
Edward knows that NSA agents use the following algorithm to cipher their messages. <br>
<br>
1) They delete all spaces and punctuation marks.<br>
2) They replace all successive identical letters with only one such letter.<br>
3) They insert two identical letters at an arbitrary place many times.<br>
<br>
Edward has intercepted some messages which are "meaningless" sequences of letters that NSA agent Bob has sent to other NSA agent Alice about possible Edward’s location. He wants to be able to restore the message as it was after step 2). Help Edward write a program in Python that removes all pairs of identical letters from the message inserted in the third step. <br>
<br>
The program should be executed by calling 'python edward.py cipheredmessage.txt' from Unix shell where "cipheredmessage.txt" is the name of a file with a ciphered message sent by Bob. The message consists of lowercase English letters and its length is at most 100 000. Output the message after step 2). The program should produce an answer in less than a few seconds.<br>

