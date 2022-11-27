import praw
import random
import datetime
import time
import markovify

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "[TITLE] Kelly [VERB] on [NOUN] that he was going to run [MARATHON]. [NEWS] reached out for comment, but the [TITLE2] declined.",
    "During a [SPEECH], Mark Kelly expressed his [AMAZEMENT] to an unsuspecting group of [ELDERLY]. He said they need to [VERB2] in order to [WHAT]. The group declined, stating that they had [WHAT2].",
    "When asked which conspiracies were true by [REPORTER], Kelly said \"[CONSPIRACY].\" According to [REDDITERS], this conspiracy theory has been thoroughly debunked. After getting a stern talking to by his [MOTHER], Kelly [WHAT3].",
    "Senator Kelly drafted a new bill that would [ACTION] funding for [BILL] and [ACTION2] spending on [BILL2]. When asked for the definition of [BILL2], Kelly said to \"[RESPONSE]\". Representatives for [BILL] said they were [RESPONSE2] with the bill.",
    "Republican challenger [OPPONENT] said duing a [SPEECH] that Mark Kelly supported [ISSUE]. In response, Kelly [RESPONSE3]. The [NEWSPAPER] documented the event with the headline, \"Kelly [HEADLINE] [OPPONENT].\"",
    "On his first day of the new term, a constituent apporached Senator Kelly and asked for [DIRECTION] [ITEM] in [PLACE]. Kelly thought it was a [ADJECTIVE] idea, but explained that [BUDGET] are eating up the state budget." 
]

replacements = {
    'TITLE' : ['Mark', 'Senator', 'Congressman', 'Commander', 'Captain', 'Incumbant'],
    'VERB' : ['announced', 'tweeted', 'whispered', 'shouted', 'declared', 'swore'],
    'NOUN' : ['the ISS', 'the Moon', 'Thursday', 'Monday', 'his mama'],
    'MARATHON' : ['a marathon', 'for president', 'over his political opponent', 'on Mars', 'a Ponzi scheme'],
    'NEWS' : ['CNN', 'FOX', 'MSNBC', 'Breitbart', 'Korean Central Television'],
    'TITLE2' : ['senator', 'congressman', 'commander', 'captain'],
    'SPEECH' : ['speech', 'debate', 'press conference', 'speed eating competition', 'thing that Arizonians do', 'campaign event', 'attack ad'],
    'AMAZEMENT' : ['amazement', 'dissapointment', 'disgust', 'gratitude'],
    'ELDERLY' : ['elderly people', 'pigeons', 'Italians', 'Chipotle workers'],
    'VERB2' : ['repent', 'ascend a mountain', 'tie their shoes', 'vote for him', 'volunteer'],
    'WHAT' : ['save democracy', 'turn the tide of the war', 'be a good friend', 'understand the truth', 'ignite the light and let it shine', 'survive', 'fall asleep tonight'],
    'WHAT2' : ['every right to ignore him', 'a baby', 'COVID', 'a friend who spoke Spanish', 'enough on their plate', 'twelve dollars'],
    'REPORTER' : ['Chris Wallace', 'Rachel Maddow', 'Clark Kent', 'George Will', 'Carl Bernstein', 'Doris Burke'],
    'CONSPIRACY' : ['all of them', 'the election was stolen', 'the moon landing was fake', 'the Earth is flat', 'dryers transport socks to different dimensions', 'Febreze has three e\'s'],
    'REDDITERS' : ['Redditers', 'fact checkers', '4chan forums', 'my uncle', 'academics'],
    'MOTHER' : ['mother', 'constituency', 'wife', 'Fortnite squad', 'advisors', 'lawyers', 'campaign manager'],
    'WHAT3' : ['apologized', 'doubled down', 'made some soup', 'wrote an optimizing compiler in Brainfuck', 'flew a T-38 really fast while listening to Frank Ocean'],
    'ACTION' : ['increase', 'decrease', 'limit', 'cut', 'expand', 'triple', 'gut', 'double'],
    'ACTION2' : ['increase', 'decrease', 'limit', 'cut', 'expand', 'triple', 'gut', 'double'],
    'BILL' : ['veterans', 'NASA', 'me', 'homeless people', 'private prisons'],
    'BILL2' : ['flood insurance', 'the Pentagon', 'food stamps', 'the Secret Serivce', 'daywalkers'],
    'RESPONSE' : ['Google it', 'look it up', 'not worry about it', 'ask your local librarian', 'please go away'],
    'RESPONSE2' : ['pleased', 'dissapointed', 'angry', 'excited about', 'frustrated'],
    'OPPONENT' : ['Blake Masters', 'Donald Trump', 'Jimmy Carter', 'Greta Thunberg', 'Sarah Palin', 'Mickey Mouse'],
    'ISSUE' : ['gun control', 'a woman\'s right to choose', 'the ACA', 'climate prevention measures', 'defunding air traffic control towers', 'grease fires'],
    'RESPONSE3' : ['laughed', 'fired back', 'agreed', 'claimed it was \"fake news\"', 'yawned', 'fell over', 'nodded', 'said \"Uhh, yes?\"'],
    'NEWSPAPER' : ['New York Times', 'Washington Post', 'Boston Globe', 'LA Times', 'Sun', 'Student Life', 'Golden Antlers'],
    'HEADLINE' : ['SLAMS', 'BLASTS', 'GRILLS', 'OWNS', 'DESTROYS'],
    'DIRECTION' : ['more', 'less', 'additional', 'better', 'fewer'],
    'ITEM' : ['stop signs', 'schools', 'police officers', 'homeless shelters', 'street racing events'],
    'PLACE' : ['Arizona', 'Phoenix', 'Scottsdale', 'Tucson', 'the Grand Canyon'],
    'ADJECTIVE' : ['great', 'horrible', 'incredible', 'disturbing', 'stupid', 'wonderful'],
    'BUDGET' : ['tourists', 'rats', 'golf courses', 'old people', 'pothole repairs'],
    }

def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib

def generate_markovify():
    with open(r"C:\Users\Ben\OneDrive\Desktop\dorling-betterpolitics.txt", encoding="utf-8") as f:
        text = f.read()

    with open(r"C:\Users\Ben\OneDrive\Desktop\locke.txt", encoding="utf-8") as f:
        text += f.read()

    with open(r"C:\Users\Ben\OneDrive\Desktop\ConLaw Essay 2.txt", encoding="utf-8") as f:
        text += f.read()

    comment= findcomment

    # Build the model.
    text_modelA = markovify.Text(text)
    modelB = markovify.Text(comment)

    model_combo = markovify.combine([ text_modelA, modelB ], [ 1, 3])

    # Print five randomly-generated sentences
    for i in range(5):
        markreply = model_combo.make_sentence()
    return markreply


# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot', user_agent='cs40')

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/ywivox/project_4_reddit/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

while True:
#if True:
    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time

    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    
    #all_comments = []
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author)!='swampboybot':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        
        text = generate_comment()
        submission.reply(text)
        time.sleep(10)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []

        for comment in not_my_comments:
            replied = False
            for reply in list(comment.replies):
                if str(reply.author)=='swampboybot':
                    replied = True
            if replied == False:
                comments_without_replies.append(comment)

    # extra credit 3 - reply to the most highly upvoted comment

    
    num_upvotes = 0
    high_up_no_reply = []
    for comment in comments_without_replies:
        if comment.score>num_upvotes:
            high_up_no_reply = [comment]
            num_upvotes = comment.score
        else:
            if comment.score == num_upvotes:
                high_up_no_reply.append(comment)


        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
    print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
    #for comment in comments_without_replies:
    if len(comments_without_replies) > 0:
        try:
            findcomment = comment.body
            random.choice(comments_without_replies).reply(generate_markovify())
        except praw.exceptions.APIException:
            print('sleeping for 5 seconds')
            time.sleep(5)

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    
    subreddit = reddit.subreddit("cs40_2022fall")
    hot = list(subreddit.hot(limit=5))
    submission = random.choice(hot)
    
    #pass

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(1)
