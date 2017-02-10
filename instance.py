import fresh_tomatoes
import movieWebsite

Toy_story = movieWebsite.Movie("TOY STORY",
                            "story of a boy and his toys",
                            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://youtu.be/KYz2wyBy3kc")
                                                       
                            

#print(Toy_story.storyline)
#Toy_story.show_trailer()

Dangal = movieWebsite.Movie("Dangal",
                            " story of two girl wrestlers",
                            "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
                            "https://youtu.be/x_7YlGv9u1g")
Pink_panther = movieWebsite.Movie("THE PINK PANTHER",
                                  "THE FUNNY MAN",
                                  "https://upload.wikimedia.org/wikipedia/en/f/f2/Pinkpanther_mp.jpg",
                                  "https://youtu.be/HokdJyD605U")
The_Hangover = movieWebsite.Movie("THE HANGOVER",
                                  " about a man and his hangover days",
                                  "http://resizing.flixster.com/SfdGaeU58BcILIBNNHXlJ_xAHLw=/800x1200/v1.bTsxMTE2NjcxNztqOzE3Mjg2OzIwNDg7ODAwOzEyMDA",
                                  "https://youtu.be/snlWDffZfyk")
Blended = movieWebsite.Movie("BLENDED",
                             " about two people",
                             "http://resizing.flixster.com/g2mvmas1ncyr_tMOlMuAUpzjqdY=/800x1200/v1.bTsxMTE4MDEzNztqOzE3Mjk2OzIwNDg7ODAwOzEyMDA",
                             "https://youtu.be/2IOQf4oHZrw")
Croods = movieWebsite.Movie("THE CROODS",
                            " An animated movie",
                            "http://www.focusonanimation.com/wp-content/uploads/2013/02/LesCROODS-120x160-Teaser_hdef.jpg",
                            "https://youtu.be/VeG3Zmk08UU")
Minions = movieWebsite.Movie(" THE MINIONS",
                             " an animated movie about minions",
                             "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTgPXOAXdAMlmpk_DODqRLToW3p49JbXE2myQ_hGTxFi1TxhcN5",
                             "https://youtu.be/P9-FCC6I7u0")
                


#print(Dangal.storyline)
#Dangal.show_trailer()
#movielist = [Toy_story,Pink_panther,Blended,Croods,Minions]
#fresh_tomatoes.open_movies_page(movielist)
print(movieWebsite.Movie.RATINGS)
