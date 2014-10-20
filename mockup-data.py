def main():
    businesses = "cheese-board-pizza-berkeley"
    #api_calls = []
    #for name in businesses:
    #    api_calls.append(get_results_biz(name))
    #    #Be a good internet citizen and rate-limit yourself...ya know for the 10000 limit
    #    time.sleep(1.0)

    biz_results = get_results_biz(businesses)
    competition_results = competition("sliver-pizzeria-berkeley-2");
    fb_info = facebook_page_info("sliver") #dict of comment to list of [type, number of likes, number of comments]

    #biz_results and competition_results [reviews, average ratings, ratings]
    average = biz_results[1]
    absolute = biz_results[2]

    print (getNorm(average,absolute) * 5) - (getNorm(average,absolute) * 5) % 0.5

    average = competition_results[1]
    absolute = competition_results[2]

    print getNorm(average, absolute) * 5 - (getNorm(average, absolute) * 5)%0.5

    print get_fb_info();


def getNorm(average, absolute):
    NormRate = {};
    total = 0
    sumAll = 0
    for name in average:
        NormRate[name] = absolute[name] - average[name]
        sumAll += NormRate[name]
        total += 1
    return sumAll/total


def get_fb_info():
    posts = facebook_page_info("sliver")
    social = [0,0]
    food = [0,0]
    total_social = 0;
    total_food = 0;
    for post in posts:
        if(posts[post][0] == "social"):
            social[0] += posts[post][1]
            social[1] += posts[post][2]
            total_social+= 1
        else: #if posts[post][0] = "food"
            food[0] += posts[post][1]
            food[1] += posts[post][2]
            total_food += 1
    social_likes = 1.0 * social[0]/total_social #social likes
    social_comments =  1.0 * social[1]/total_social #social comments
    food_likes = 1.0 * food[0]/total_food # food likes
    food_comments =  1.0 * food[1]/total_food # food comments

    comments = ""

    if(social_likes > 5):
        if(food_likes > 5):
            comments += "Customers enjoy both your food and atmosphere, "
            if(food_likes > social_likes):
                comments += "but your food is more talked about!"
            else: 
                comments += "but your atmosphere is more talked about!"
        else:
            comments += "Customers enjoy your atmosphere, but not as much the food"
    else:
        if(food_likes > 5):
            comments += "Customers enjoy your food, but you should improve the atmosphere of your business"
        else:
            comments += "Both atmosphere and food need improving"

    all_foods = []
    for post in posts:
        all_foods.append(post)

    wanted = []
    for i in all_foods:
        if(i[0:16] == "Pizza of the Day"):
            wanted.append(i)

    hashIngred = {}
    allIngredients = []
    for food in wanted:
        allIngredients = allIngredients + sliceFood(food);
    for i in allIngredients:
        if(i in hashIngred):
            hashIngred[i] = hashIngred[i] + 1
        else:
            hashIngred[i] = 1
    
    bestNum = 0
    best = ""
    for i in hashIngred:
        if(hashIngred[i] > bestNum):
            best = i
            bestNum = hashIngred[i]

    print best

    return comments


def sliceFood(foodName):
    index = 0;
    for i in range(len(foodName)-1):
        index += 1
        if(foodName[i:i+1] == ":"):
            break

    foodName = " " + foodName[index: len(foodName)]

    ingred = []
    index = 0
    for i in range(len(foodName)-1):
        if(foodName[i:i+1] == ","):
            ingred.append(foodName[index +2 :i])
            index = i

    return ingred


def facebook_page_info(name):
    posts = {}
    posts["Pizza of the Day Sunday: Fresh Corn, Zucchini, Onions, Mozzarella and French Feta Cheese, Cilantro , Limes, Garlic Olive Oil."] = ["food", 7, 0]
    posts["Saturday, Oct. 18 Fresh Cremini Mushrooms, Onions, Green Bell Peppers, Mozzarella and French Feta Cheese, Italian Parsley, Garlic Olive Oil"] = ["food", 2, 0]
    posts["Cal vs. UCLA today at 12:30! Beat LA"] = ["social", 3, 0]
    posts["Willy making your pizzas hot and fresh!"] = ["social", 24, 0]
    posts["Pizza of the Day Thursday: Fresh Corn, Red Bell Pepper, Onions, Mozzarella, Cotija Cheese, Cilantro Avocado Pesto, (no nuts)"] = ["food", 2, 1]
    posts["Pizza of the Day Wednesday: Roma Tomatoes, Red Onion, Mozzarella and French Feta Cheese, Kalamata and Green Olive Tapenade."] = ["food", 5, 0]
    posts["Pizza of the Day Tuesday: Roasted Potatoes, Roasted Onions, Chile Pasilla, Mozzarella and French Feta Cheese, Cilantro, Limes, Garlic Olive Oil. Go Giants!!"] = ["food", 6, 0]
    posts["Let's go Niners! Gold Rush at Sliver today!"] = ["social", 7, 0] 
    posts["Monday, Oct. 13 Fresh Corn, Zucchini, Onions, Mozzarella and French Feta Cheese, Cilantro , Limes, Garlic Olive Oil."] = ["food", 17, 0]
    return posts

def competition(name):
    data = []
    data.append("What else can I add that hasn't already been said? A great pizza place. Pizza tastes great - never disappoints. It can also serve a good rendezvous if you wanna watch sports with friends in a public place. Great atmosphere, too!  Whenever there's a long queue of pizza orders (especially if someone in front of you just ordered 3+ pies), the establishment is considerate. They'll give you a sliver of pizza for your trouble. This is IN ADDITION to the sliver pieces that you're gonna get, anyway! Pretty cool.The only possible complaint I can think of is that I wish their cups for the water are bigger. They're so small! I find myself just bringing two cups back to the table, both of them for me, just so that I don't have to get up again (if I'm lucky.) But that's a minor complaint - could be easily fixed in a jiffy.TIP: Maybe I've just been in a lucky stride lately, but you oughta order to-go always, even if you plan to eat there anyway. In my experience, if I order 3 slices, I always obtained an additional 3 sliver slices. I noticed that if I order for here, if I order that same amount of 3 slices, I'd maybe get 1 or 2 sliver slices. The more, the merrier, right? To-go is the way to go!")
    data.append("Sliver serves a sub-$4 slice in a casual indoor-outdoor eatery that opens onto bustling Center Street. It's a definite go-to if you're looking for a pizza-and-draft on a busy Sunday Streets afternoon in Berkeley. There's a small sit-down bar at the front with beer taps and you'll order at the counter. Dogs are OK at the sidewalk tables. We stopped in while couples were salsa dancing in the street. The scene was lively and perfect for an outdoor meal. Our slice, actually three randomly-cut pieces of pizza, was nonetheless delicious and repeatable. We washed it down a pair of draft IPAs -Luci's choice, a Deschutes Fresh Squeezed IPA, and mine, Lagunitas Hop Stoopid. What's not to like here? We're comin back!")
    data.append("SO GOOD! I'm highly torn between Cheeseboard and Sliver but I LOVE BOTH regardless if the owners hate each other as the myth goes.  The amazing thing about sliver definitely would have to be it's LOCATION, so much closer to the CAL campus. Definitely wish I had this when I was a student. And most importantly..... UNLIMITED SELF SERVE CILANTRO SAUCE!!!!! I'm highly biased since I wish I could marry CILANTRO. But seriously, DAT SAUCE is amazing! DRENCH YOUR PIZZA WITH IT. Also the WINE AND BEER bar paired with the pizza is just too damn amazing!")
    data.append("Pretty much The Cheese Board on Center Street.  Like this location better, the large screen tv's, the sangria and the cilantro sauce.  And of course that little sliver sample you get.")
    data.append("I think Sliver is underrated. It's the little sister of Cheesboard, but less crowded, more beer, and if you're into sports, tvs to watch games. They also have wifi, which I dig. The people watching is awesome, if you can snag a spot outside. Same deal as Cheesboard: one pizza, one salad, get it and sit your ass down. The ingredients are amazing, and you still get the tiny piece on top of whatever you order. Bonus. The good: great pizza, great business. They have a social justice component that I dig. The bad: the tv can be kind of loud, but just stay away if there's a major sports game. :)")
    data.append("I came here on a Saturday before the Cal football game and it was probably the best thin crust pizza I've ever had. They only serve one flavor of pizza a day and each order comes with a sliver of pizza. This restaurant is located walking distance from the Downtown Berkeley BART Station and I would highly recommend it!")
    data.append("Sliver is centrally located with super nice staff. Lines move quickly. They are very efficient.For lunch, they have a pizza and salad combo for $5! Love it as they carry vegetarian pizzas!   5 stars!  They combine different unusual kind of cheeses and veggies for their pizza.I love the pesto green hot sauce. It makes my day!Complimentary war is also chilled. Outdoor and indoor seating available for people watching.")
    data.append("Ordered: Fresh Corn, Roasted Potatoes, Mozzarella and Bulgarian Feta Cheese, Cilantro, Lime Juice, Garlic Olive Oil What to get: depends on the day! Check out the website or their feeds for the pizza of the day. This pizza was kind of dry and was missing something sweet/savory for me. The crust was still the same like that of Cheese Board. Sliver overall is great!")
    data.append("Fantastic place! Great live jazz on Friday/Saturday, delicious pizza and Sierra Nevada Hefeweizen on tap :). They could hold out on the olive oil though; not really needed with their tasty creations :)")
    
    averageRatings = {}
    averageRatings["Dale C."] = 3.201
    averageRatings["Paul M."] = 3.234
    averageRatings["John H."] = 4.434 # over
    averageRatings["Steve C."] = 2.435
    averageRatings["Kristin U."] = 4.237
    averageRatings["Amanda B."] = 3.987
    averageRatings["Karen L."] = 4.873
    averageRatings["Kitty T."] = 3.876
    averageRatings["James N."] = 4.021 #lil over

    ratings = {}
    ratings["Dale C."] = 5
    ratings["Paul M."] = 5
    ratings["John H."] = 4
    ratings["Steve C."] = 5
    ratings["Kristin U."] = 5
    ratings["Amanda B."] = 5
    ratings["Karen L."] = 5
    ratings["Kitty T."] = 5
    ratings["James N."] = 4

    output = []
    output.append(data)
    output.append(averageRatings)
    output.append(ratings)

    return output



#********************** search ***********************************


#********************** biz *******************************

def get_results_biz(id):

    
    data = []
    data.append("I come to Berkeley quite a bit but somehow I ALWAYS missed out on coming here for a variety of reasons (but mostly due to their limited hours/being closed on Sundays) so I was SOOOO happy to finally be able to come here. Of course I came on a day where all the UCLA people were up to watch the game so the line wrapped around the entire building to the end of the block. Even though the line was super long I don't think we waited more than 30 minutes. Service was rushed but friendly. But more importantly: the pizza. I was so excited to have a piece that I started eating my to-go order as we walked to the car. It was sooooo good. We got the last corn pizza of the year and everything about it was amazing. I loved that the crust was thin, the balance of cheese was amazing, and everything was just perfect. I wish my friends and I actually got to eat at the restaurant. The entire place was bustling and the music was fantastic but finding a spot to sit was too hard. Overall I would LOVE to come back. If only the business hours were better. :/")
    data.append("$2 for a giant slice and a tiny extra slice on top! They only serve one flavor a day and theres always a line wayy out the door! It's worth it if you have a Saturday all to your leisure :) The service is friendly and the seating is open with both indoor and outdoor. Cute old peple play the live band.")
    data.append("My husband, Kids and I came here about 2 Friday's ago. It was our first time there. We get to the location and the line is crazy long which went by pretty fast and they had a live band. Upon getting close to the front door I kept seeing a lot of people walking out with the same pizza slice. Then we get to the door and realize that they have only one type of pizza a day. I still wanted to make sure though so when we get to the register I ask the lady if they had pepperoni and she said no and confirmed that its a certain pizza a day. Well that was not gonna work for us since my 6 year old is very picky. So we told her we had to pass and she gave us 2 slices to try for free after we told her it was our first time there and also said that if after tasting it we decide we want to order we could just go to the front of the line...super nice. Anyway the pizza that day had butternut squash and other toppings that I forgot and I ate it so quick because it was so good. If we didn't have the kids I would definitely had gone to order. Next time we will go without the kids. =)")
    data.append("Came here 3 times in 4 days. It's that good! Expect a significant, but fast-moving line, a different kind of white pizza every day, and a fair bit of cheesy greasy goodness. Usually some kind of green sauce (cilantro, pesto, etc) on the pizza, but the cheese is the focus here. Different music acts every day for both lunch and dinner hours; saw some awesome, soulful bossa nova stuff here -- as well as some more average stuff.  Closes early at 8pm. The line looks crazy long, but it moves quickly because they only have one pizza per day. My man and I ordered a full pizza and bam it was handed to us, with a couple extra tiny slices on top. It was way more food than we needed and ended up taking home leftovers. With the extra slices we could have been just fine with a half pie between the two of us. The live band was alright, we were able to find a seat ok. We'll be back. Gluten free pizza is awesome but when they say 10-15 minutes you should expect 15-20. Still, some of the best gluten free pizza I've had ANYWHERE!")
    data.append("This is a truly original place to get pizza. Today they were serving up California corn slices. The serving was one big slice and one half slice. I had never had corn on pizza. The crust is crispy and solid, not too thin or too fluffy. The cheese is harder and a little chunky...not light. It's hard to describe, so you should try it yourself! It came with some lime slices and the lime juice made the pizza incredible. There's also a cheese shop and bakery next door. Amazing offering in the town of Berkeley. It really adds to the classiness and tastefulness of the town. Cheeseboard pizza is a must visit when in Berkeley.")
    data.append("Best pizza I've ever had in my life! Don't let the long line intimidate you. It goes by quickly. I'm convinced that there is a pizza chemist in their back kitchen! Literally every pizza they make is made to perfection! No matter how weird the ingredients may sound together in a pizza, just trust them and eat it. It's worth everything in your life. I love you, Cheeseboard.")
    data.append("The line looks crazy long, but it moves quickly because they only have one pizza per day. My man and I ordered a full pizza and bam it was handed to us, with a couple extra tiny slices on top. It was way more food than we needed and ended up taking home leftovers. With the extra slices we could have been just fine with a half pie between the two of us. The live band was alright, we were able to find a seat ok. We'll be back.")
    data.append("Fresh made thin crust pizza. One flavor each day. Quality ingredients. They are generous with the olive oil. Some people might find it oily. Best when immediately consumed. Good service. Long line that moves relatively quick. Energetic live music. Good bathrooms.")
    data.append("Cheese Board is good. I enjoy that they have a daily seasonal menu. Not sure if it's worth the wait and the live music can be a little blast your ears off loud...in my opinion a little loud for such a small space. All in all I'd happily eat their pizza but I wouldn't wait in an hour long line to get it.")
    data.append("Never a fan of vegetarian pizza but this place is something else. Wonderful creativity with the daily pizza recipes. Service is great even when queue can be long - pizza was served immediately after payment. Will definitely come here again.")
    data.append("Ordered: dry farmed Romanita tomato (from Oya organic farm) and San Marzano tomato (from Ambrosio organic farm), red onion, mozzarella and Belgioioso aged asiago cheese, garlic olive oil, and fresh herbs What to get: depends on which day you go, since they serve one type a day This place probably makes a killing, considering how fast they serve people. The wait in line actually isn't that long. Once you hit the register, they have your pie ready. This pizza I liked. If Cheese Board doesn't have the one you want that day, go check out Sliver Pizzeria, pretty much the same thing.")

    averageRatings = {}
    averageRatings["Vivian C."] = 3.243
    averageRatings["Diana S."] = 3.623
    averageRatings["Anna G."] = 3.869
    averageRatings["Pete S."] = 3.021
    averageRatings["Denise C."] = 4.089
    averageRatings["Denyse E."] = 2.980
    averageRatings["Katie C."] = 3.281
    averageRatings["Harry P."] = 5 #harry voted lower
    averageRatings["Maci B."] = 4.978

    ratings = {}
    ratings["Vivian C."] = 5
    ratings["Diana S."] = 4 
    ratings["Anna G."] = 4
    ratings["Pete S."] = 5
    ratings["Denise C."] = 5
    ratings["Denyse E."] = 5
    ratings["Katie C."] = 5
    ratings["Harry P."] = 4
    ratings["Maci B."] = 5

    output = []
    output.append(data)
    output.append(averageRatings)
    output.append(ratings)

    return output

    #return data

if __name__=="__main__":
    main()