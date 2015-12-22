Character Swap
====================

An entry in [NaNoGenMo 2015](https://github.com/dariusk/NaNoGenMo-2015/).

This program can be used to swap the names and gendered pronouns of characters 
in a novel to experience the book from a different perspective.

The program creates multiple versions of a book:

* Opposite: where all the characters have been swapped to a version of themselves using the opposite pronouns. 

  >She was a remarkably handsome woman dark, aquiline, and moustached–evidently the woman of whom I had heard.
  
  >Oh, he has turned all the women’s heads down in that part. He is the daintiest thing under a bonnet on this planet.
  
* They: where all the characters have been swapped to a version of themselves using they pronouns.

  >Grit in a sensitive instrument, or a crack in one of their own high-power lenses, would not be more disturbing 
  than a strong emotion in a nature such as their. And yet there was but one person to them, and that person was the 
  late Eren Adler, of dubious and questionable memory.
  
* She: where all the characters have been swapped to a version of themselves using she pronouns. 

  >I entered my consulting-room and found a gentlewoman seated by the table. She was quietly dressed in a suit of 
  heather tweed with a soft cloth cap which she had laid down upon my books. Round one of herr hands she had a 
  handkerchief wrapped, which was mottled all over with bloodstains. She was young, not more than five-and-twenty, 
  I should say, with a strong, feminine face; but she was exceedingly pale and gave me the impression of a woman who 
  was suffering from some strong agitation, which it took all herr strength of mind to control.
  
* He: where all the characters have been swapped to a version of themselves using he pronouns.

  >One night — it was in June, ’89 — there came a ring to my bell, about the hour when a man gives his first yawn and 
  glances at the clock. I sat up in my chair, and my husband laid his needle-work down in his lap and made a little 
  face of disappointment.
  “A patient!” said he. “You’ll have to go out.”
  I groaned, for I was newly come back from a weary day. We heard the door open, a few hurried words, and then quick 
  steps upon the linoleum. Our own door flew open, and a lord, clad in some dark-coloured stuff, with a black veil, 
  entered the room.
  “You will excuse my calling so late”, he began, and then, suddenly losing his self-control, he ran forward, threw 
  his arms about my husband’s neck, and sobbed upon his shoulder.
  “Oh, I’m in such trouble!” he cried; “I do so want a little help.”
  “Why,” said my husband, pulling up his veil, “it is Kyle Whitney. How you startled me, Kyle! I had not an idea who 
  you were when you came in.”
  “I didn’t know what to do, so I came straight to you.”
  That was always the way. Folk who were in grief came to my husband like birds to a light-house.

* Skin Color: the text is modified and augmented to create a version where the characters have different skin colors.
  These texts are created in the same folder and named Reskinned_(pronoun)_(book name).txt
 
  >He opened a locket and showed us the full bronzed face of a very lovely man. It was not a photograph but an ebony 
  miniature, and the artist had brought out the full effect of the lustrous black hair, the large dark eyes, and the 
  exquisite mouth.

  >"Let us have everything in its due order."  Holmes thrust his long thin caramel legs out towards the fire and composed  
  himself to listen.



To change the book to be analyzed, create a folder for the book and add the book as a text file 
to that folder. Create a names folder inside the book folder and add four name csv files to that folder
with the character names and the name changes you'd like, and create a python file similar to holmesSwap.py 
in the book folder. Change the file name text in the main function in the python file to the name of the book, 
and run the program. The program takes around 30 minutes to complete. 


References
==========

The Adventures of Sherlock Holmes
---------------------------------

This and all associated files of various formats can be found at:
http://www.gutenberg.org/ebooks/1661

Frankenstein
------------
This and all associated files of various formats can be found at:
http://www.gutenberg.org/ebooks/84

These eBooks are for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License online at 
www.gutenberg.org


License
=======

Copyright 2015 Emily Daniels

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.