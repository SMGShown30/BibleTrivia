# TREENODE CLASS
class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while len(story_node.choices) > 0:
            user_input = input("Enter 1 or 2 to continue the story: ")
            if user_input not in ["1", "2"]:
                print("Enter a valid choice")
            chosen_index = int(user_input)
            chosen_index -= 1
            chosen_child = story_node.choices[chosen_index]
            print(chosen_child.story_piece)
            story_node = chosen_child


# VARIABLES FOR TREE
print("Rise to Greatness: The Chosen One")
user_choice = input("What is your name? ")
print(f"{user_choice}, this is the beginning of your story to the NBA.")

# TESTING AREA
story_root = TreeNode(f"""
{user_choice}, you are a rising senior in high school.
So far, you have zero offers, and it seems as though your NBA dreams are coming to an end.
You decide to leave your current high school to transfer to a new school in hopes that the new environment will get you an offer.
Which school do you pick:
1) Marian Catholic HS in Chicago Heights, IL
2) Thownwood HS in South Holland, IL
""")
choice_Marian = TreeNode(f"""
You chose Marian Catholic.
You meet the head coach, Coach Taylor.
He says, "Welcome to Marian, {user_choice}.
We prioritize team development here.
Do you:
1) Decide to continue to work on your skill development despite Coach saying that isn't necessary.
2) Conform to the system.
""")
choice_Twood = TreeNode(f"""
You chose Thownwood.
You meet the head coach, Coach Simmons.
Welcome to Twood!
We prioritize player development here.
Do you:
1) Decide to continue to work on your team development despite Coach saying that isn't necessary.
2) Conform to the system.
""")
choice_Marian_1 = TreeNode("""
You chose skill development.
You decided to grind before the season started and became an excellent ball handler and elite shooter.
The day of tryouts comes.
You feel very prepared since you have worked on your skills.
You do extremely well in tryouts, and the coach is shocked by how good you are.
However, although you are very good, he heavily criticizes your lack of team play.
Despite the criticism, you still make the team, but the coach says that you won't get many, if any, minutes.
Do you:
1) Badmouth the coach and say that he doesn't know what he's talking about. Skill development is more important, ignoring team play.
2) Decide to work extremely hard and learn how to be a better team player.
""")
choice_Marian_2 = TreeNode("""
You chose to focus on team development.
Tryouts come around, and you are making plays left and right, setting up your teammates.
However, your shooting and ball handling are mediocre.
Coach loves the way you fit the team's playstyle and says that you will be in the rotation.
Coach says, "I don't think you'll get an offer, but you will be a good basketball player."
This is not what you transferred for.
Do you:
1) Go against your own personal goals and go with the flow.
2) Try to work on your skills in the weeks before the first game.
""")
choice_Twood_1 = TreeNode("""
You work to become a better team player.
Tryouts come, and you don't look impressive to Coach.
He wants you to be a scorer on the team, especially if you want a scholarship.
You barely make the team, and minutes aren't promised to you.
Do you:
1) Work on your skills, even though it is kind of late for that now.
2) Rock with what you've got and play your way, focusing on team-oriented basketball.
""")
choice_Twood_2 = TreeNode(f"""
Tryouts come, and you are miles above everyone else.
You can score at will. Even though you are selfish with the ball, Coach doesn't care because you can shoot the lights out.
Your teammate walks up to you and says, "{user_choice}, you need to be a better team player if you want attention from college coaches."
Do you:
1) Brush off his advice.
2) Take his advice seriously and watch film on how to be a better playmaker on the basketball court.
""")
choice_Marian_1_1 = TreeNode("""
You decide to badmouth the coach and insist that skill development is more important.
Coach is offended by your attitude and bench you for the entire season.
You don't receive any scholarship offers, and your NBA dreams fade away.

GAME OVER. You didn't reach the NBA.
""")
choice_Marian_1_2 = TreeNode("""
You choose to work extremely hard and learn how to be a better team player.
You dedicate yourself to understanding the coach's system and improve your passing and decision-making skills.
As the season progresses, you become a key playmaker for the team and receive attention from college scouts.
You receive multiple scholarship offers and ultimately make it to the NBA.

CONGRATULATIONS! You have reached the NBA.
""")
choice_Marian_2_1 = TreeNode("""
You go with the flow and suppress your personal goals.
The team performs well, and you contribute as a role player.
Although you don't receive any scholarship offers, you gain valuable experience and develop as a team player.

YOU HAVE MADE PROGRESS TOWARDS YOUR NBA DREAM.
""")
choice_Marian_2_2 = TreeNode("""
You decide to work on your skills in the weeks before the first game.
You spend countless hours refining your shooting and ball handling abilities.
When the season begins, you amaze everyone with your improved skills.
You receive attention from college scouts and receive scholarship offers.

CONGRATULATIONS! You have reached the NBA.
""")
choice_Twood_1_1 = TreeNode("""
You work on your skills despite it being late in the process.
You put in extra hours at the gym and show significant improvement.
Coach recognizes your dedication and gives you more playing time.
Your performances catch the attention of college coaches, and you receive scholarship offers.

CONGRATULATIONS! You have reached the NBA.
""")
choice_Twood_1_2 = TreeNode("""
You rock with what you've got and play your way, focusing on team-oriented basketball.
Although you don't score much, you excel as a team player and contribute to the team's success.
Your unselfish style of play impresses college scouts, and you receive scholarship offers.

CONGRATULATIONS! You have reached the NBA.
""")
choice_Twood_2_1 = TreeNode("""
You brush off your teammate's advice and continue to play selfishly.
While you score many points, your individualistic approach hinders team chemistry.
As a result, the team struggles, and you don't receive any scholarship offers.

GAME OVER. You didn't reach the NBA.
""")
choice_Twood_2_2 = TreeNode("""
You take your teammate's advice seriously and watch film to become a better playmaker.
You develop your passing skills and basketball IQ, becoming a well-rounded player.
College coaches are impressed by your improved game, and you receive scholarship offers.

CONGRATULATIONS! You have reached the NBA.
""")

story_root.add_child(choice_Marian)
story_root.add_child(choice_Twood)

choice_Marian.add_child(choice_Marian_1)
choice_Marian.add_child(choice_Marian_2)

choice_Twood.add_child(choice_Twood_1)
choice_Twood.add_child(choice_Twood_2)

choice_Marian_1.add_child(choice_Marian_1_1)
choice_Marian_1.add_child(choice_Marian_1_2)

choice_Marian_2.add_child(choice_Marian_2_1)
choice_Marian_2.add_child(choice_Marian_2_2)

choice_Twood_1.add_child(choice_Twood_1_1)
choice_Twood_1.add_child(choice_Twood_1_2)

choice_Twood_2.add_child(choice_Twood_2_1)
choice_Twood_2.add_child(choice_Twood_2_2)

story_root.traverse()
