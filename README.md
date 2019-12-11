# 4300Final

The following Readme provides detailed documentation on what our HTML and APIs do, as well as how to utilize each of them.

*HTML*
-index.html:
	-URI: http://172.17.152.127/final/
	-This is our home page, which has 2 buttons. One leads to our type advantage calculator, and the other leads to our generation game finder. 

-typeAdv.html
	-URI: http://172.17.152.127/final/typeAdv.html
	-This page is our type advantage calculator. The user is allowed to choose between the provided types in the dropdown menues and given the corresponding effectivness of the attacking move against the defending one.
	-For example, selecting Ghost and Ghost will result in a super-effective attack. However, Fighting against Ghost will result in no effect
	-The attacking option that is chosen here sends a request to types.py with the query string "?op1=" and the name of the associating type (i.e chosing Ghost will append "Ghost" to the query string, Dark will append "Dark", etc)

-gen.html
	-URI: http://172.17.152.127/final/gen.html
	-This page is for our Pokemon generational library which will display specific games depending on the chosen generation.
	-For example, selecting Generation 8 will result in the box art for Pokemon Sword and Pokemon Shield to be displayed.
	-The option that is chosen here sends a request to gens.py with the query string "?op1=" and the associating number (i.e Generation 1 will add "1" to the query string, Generation 2 will add "2", etc)

*API*
-gens.py
	-URI: http://172.17.152.127/gens/
	-This python application returns JSON data to the user. If no query string is specified, then the entire table is returned. 
	-If a query string is specified then it will return only the specified portion of the table.
	-The argument "op1" is taken with any of the following values: 1, 2, 3, 4, 5 ,6 ,7 ,8
	-Example:
		http://172.17.152.127/gens/?op1=3 => Will return only items with GenNumber = 3
		http://172.17.152.127/gens/ => Will return entire table regardless of GenNumber

-types.py
	-URI: http://172.17.152.127/types/
	-This python application returns JSON data to the user. If no query string is specified, then the entire table is returned.
        -If a query string is specified then it will return only the specified portion of the table.
	-The argument "op1" is taken with any of the following values: Ghost, Dark, Poison, Electric, Normal, Fire, Psychic, Flying, Ice, Dragon, Water, Fighting, Steel, Rock, Fairy, Grass, Bug, or Ground.
	 -Example:
                http://172.17.152.127/types/?op1=Ghost => Will return only rows with Types = Ghost
                http://172.17.152.127/gens/ => Will return entire table regardless of Types
