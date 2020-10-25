# Ciphered message
Edward knows that NSA agents use the following algorithm to cipher their messages. <br>
<br>
1) They delete all spaces and punctuation marks.<br>
2) They replace all successive identical letters with only one such letter.<br>
3) They insert two identical letters at an arbitrary place many times.<br>
<br>
Edward has intercepted some messages which are "meaningless" sequences of letters that NSA agent Bob has sent to other NSA agent Alice about possible Edward’s location. He wants to be able to restore the message as it was after step 2). Help Edward write a program in Python that removes all pairs of identical letters from the message inserted in the third step. <br>
<br>
The program should be executed by calling 'python edward.py cipheredmessage.txt' from Unix shell where "cipheredmessage.txt" is the name of a file with a ciphered message sent by Bob. The message consists of lowercase English letters and its length is at most 100 000. Output the message after step 2). The program should produce an answer in less than a few seconds.<br>

