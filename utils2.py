my_data = {"page":1,"results":[{"adult":"false","backdrop_path":"/qWQSnedj0LCUjWNp9fLcMtfgadp.jpg","genre_ids":[28,12,878],"id":667538,"original_language":"en","original_title":"Transformers: Rise of the Beasts","overview":"When a new threat capable of destroying the entire planet emerges, Optimus Prime and the Autobots must team up with a powerful faction known as the Maximals. With the fate of humanity hanging in the balance, humans Noah and Elena will do whatever it takes to help the Transformers as they engage in the ultimate battle to save Earth.","popularity":11856.991,"poster_path":"/gPbM0MK8CP8A174rmUwGsADNYKD.jpg","release_date":"2023-06-06","title":"Transformers: Rise of the Beasts","video":"false","vote_average":7.3,"vote_count":1304},{"adult":"false","backdrop_path":"/5YZbUmjbMa3ClvSW1Wj3D6XGolb.jpg","genre_ids":[878,12,28],"id":447365,"original_language":"en","original_title":"Guardians of the Galaxy Vol. 3","overview":"Peter Quill, still reeling from the loss of Gamora, must rally his team around him to defend the universe along with protecting one of their own. A mission that, if not completed successfully, could quite possibly lead to the end of the Guardians as we know them.","popularity":4145.055,"poster_path":"/r2J02Z2OpNTctfOSN1Ydgii51I3.jpg","release_date":"2023-05-03","title":"Guardians of the Galaxy Vol. 3","video":"false","vote_average":8.1,"vote_count":3154},{"adult":"false","backdrop_path":"/4XM8DUTQb3lhLemJC51Jx4a2EuA.jpg","genre_ids":[28,80,53],"id":385687,"original_language":"en","original_title":"Fast X","overview":"Over many missions and against impossible odds, Dom Toretto and his family have outsmarted, out-nerved and outdriven every foe in their path. Now, they confront the most lethal opponent they've ever faced: A terrifying threat emerging from the shadows of the past who's fueled by blood revenge, and who is determined to shatter this family and destroy everything—and everyone—that Dom loves, forever.","popularity":2250.479,"poster_path":"/fiVW06jE7z9YnO4trhaMEdclSiC.jpg","release_date":"2023-05-17","title":"Fast X","video":"false","vote_average":7.4,"vote_count":2737}]}


# print(type(my_data["results"]))
# print(len(my_data["results"][0]))
# print(my_data["results"][0])

for i in range(len(my_data["results"])):
    title = my_data["results"][i]["title"]
    date_released = my_data["results"][i]["release_date"]
    ratings = int(my_data["results"][i]["vote_average"])

    if ratings > 5:
        ratings = 5

    print(title, date_released, ratings)


# for i in range(3):
#     print(my_data["results"][i])



