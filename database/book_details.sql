DROP TABLE IF EXISTS authors;
CREATE TABLE authors (
  id INT AUTO_INCREMENT NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY(`id`, `name`)
);

INSERT INTO authors
  (name)
VALUES
  ('Terry Pratchett'),
  ('Neil Gaiman'),
  ('Herman Melville'),
  ('Oscar Wilde'),
  ('Kurt Vonnegut'),
  ('Ursula K. Le Guin'),
  ('Jane Austen'),
  ('Susanna Clarke'),
  ('Lauren Elkin'),
  ('Emily St. John Mandel');
  
DROP TABLE IF EXISTS titles;
CREATE TABLE titles (
  id INT AUTO_INCREMENT NOT NULL,
  title VARCHAR(255) NOT NULL,
  author_id INT NOT NULL,
  PRIMARY KEY(`id`)
);

INSERT INTO titles
  (title, author_id)
VALUES
  ('A Hat Full of Sky', 1),
  ('Bartleby, the Scrivener', 3),
  ('Breakfast of Champions', 5),
  ('De Profundis', 4),
  ('Emma', 7),
  ('Flaneuse', 9),
  ('Fragile Things', 2),
  ('Galapagos', 5),
  ('Hogfather', 1),
  ('Jonathan Strange & Mr Norrell', 8),
  ('Lords and Ladies', 1),
  ('Moby-Dick', 3),
  ('Piranesi', 8),
  ('Pride and Prejudice', 7),
  ('Reaper Man', 1),
  ('Sea of Tranquility', 10),
  ('Sense and Sensibility', 7),
  ('Slaughterhouse-Five', 5),
  ('Station Eleven', 10),
  ('The Disposessed', 6),
  ('The Farthest Shore', 6),
  ('The Happy Prince', 4),
  ('The Importance of Being Earnest', 4),
  ('The Lathe of Heaven', 6),
  ('The Left Hand of Darkness', 6),
  ('The Ocean at the End of the Lane', 2),
  ('The Ones Who Walk Away from Omelas', 6),
  ('The Picture of Dorian Gray', 4),
  ('The Sandman', 2),
  ('The Tombs of Atuan', 6);
  
DROP TABLE IF EXISTS quotes;
CREATE TABLE quotes (
  id INT AUTO_INCREMENT NOT NULL,
  quote TEXT NOT NULL,
  title_id INT NOT NULL,
  PRIMARY KEY(`id`)
);

INSERT INTO quotes
  (quote, title_id)
VALUES
  ('“As for me, I am tormented with an everlasting itch for things remote. I love to sail forbidden seas, and land on barbarous coasts.”', 12),
  ('“Birds are not difficult to understand. Their behaviour tells me what they are thinking. Generally it runs along the lines of: Is this food? Is this? What about this? This might be food. I am almost certain that this is. Or occasionally: It is raining. I do not like it.”', 13),
  ('“Books were safer than other people anyway.”', 26),
  ('“Even if it\'s not your fault, it\'s your responsibility.”', 1),
  ('“For we each of us deserve everything, every luxury that was ever piled in the tombs of the dead kings, and we each of us deserve nothing, not a mouthful of bread in hunger. Have we not eaten while another starved? Will you punish us for that? Will you reward us for the virtue of starving while others ate? No man earns punishment, no man earns reward. Free your mind of the idea of deserving, the idea of earning, and you will begin to be able to think.”', 20),
  ('“Freedom is a heavy load, a great and strange burden for the spirit to undertake. It is not easy. It is not a gift given, but a choice made, and the choice may be a hard one. The road goes upward towards the light; but the laden traveler may never reach the end of it.”', 30),
  ('“Then, one stupid person, no different from any other stupid person, wanders into your stupid life...you give them a piece of you. They don\'t ask for it. They do something dumb one day like kiss you or smile at you, and then your life isn\'t your own anymore.”', 29),
  ('“Hell is the absence of the people you long for.”', 19),
  ('“I am so clever that sometimes I don\'t understand a single word of what I am saying.”', 22),
  ('“I declare after all there is no enjoyment like reading! How much sooner one tires of any thing than of a book! -- When I have a house of my own, I shall be miserable if I have not an excellent library.”', 14),
  ('“I do not care what comes after; I have seen the dragons on the wind of morning.”', 21),
  ("“I lived in books more than I lived anywhere else.”", 26),
  ('“I think...that I would rather recollect a life mis-spent on fragile things than spent avoiding moral debt.”', 7),
  ('“I thought I was your destination. Looks like I was just another stop on the line.”', 7),
  ('“I walk because it confers- or restores- a feeling of placeness...I walk because, somehow, it\'s like reading. You\'re privy to these lives and conversations that have nothing to do with yours, but you can eavesdrop on them. Sometimes it\'s overcrowded; sometimes the voices are too loud. But there is always companionship. You are not alone. You walk in the city side by side with the living and the dead.”', 6),
  ('“I would feel infinitely more comfortable in your presence if you would agree to treat gravity as a law, rather than one of a number of suggested options.”', 29),
  ('“I would prefer not to.”', 2),
  ('“I\'VE NEVER BEEN VERY SURE ABOUT WHAT IS RIGHT, said Bill Door. I AM NOT SURE THERE IS SUCH A THING AS RIGHT. OR WRONG. JUST PLACES TO STAND.”', 15),
  ('“If I loved you less, I might be able to talk about it more.”', 5),
  ('“In the beginning there was nothing, which exploded.”', 11),
  ('“It is good to have an end to journey toward; but it is the journey that matters, in the end.”', 25),
  ('“It is sometimes a mistake to climb; it is always a mistake never even to make the attempt. If you do not climb, you will not fall. This is true. But is it that bad to fail, that hard to fall?”', 29),
  ('“It isn\'t what we say or think that defines us, but what we do.”', 17),
  ('“Light thinks it travels faster than anything but it is wrong. No matter how fast light travels, it finds the darkness has always got there first, and is waiting for it.”', 15),
  ('“Like so many other pathological personalities in positions of power a million years ago, he might do almost anything on impulse, feeling nothing much. The logical explanations for his actions, invented at leisure, always came afterwards.”', 8),
  ('“Love doesn\'t just sit there, like a stone, it has to be made, like bread; remade all the time, made new.”', 6),
  ('“My point is, there’s always something. I think, as a species, we have a desire to believe that we’re living at the climax of the story. It’s a kind of narcissism. We want to believe that we’re uniquely important, that we’re living at the end of history, that now, after all these millennia of false alarms, now is finally the worst that it’s ever been, that finally we have reached the end of the world.”', 16),
  ('“Most people are other people. Their thoughts are someone else\'s opinions, their lives a mimicry, their passions a quotation.”', 4),
  ('“Nobody gets through life without losing a few things on the way.”', 7),
  ('“Real stupidity beats artificial intelligence every time.”', 9),
  ('“So it goes.”', 18),
  ('“So, in the interests of survival, they trained themselves to be agreeing machines instead of thinking machines. All their minds had to do was to discover what other people were thinking, and then they thought that, too.”', 3),
  ('“Some things are too big to be seen; some emotions too huge to be felt.”', 29),
  ('“The books that the world calls immoral are books that show the world its own shame.”', 28),
  ('“The only thing that kept me going was stories. Stories are hope. They take you out of yourself for a bit, and when you get dropped back in, you\'re different- you\'re stronger, you\'ve seen more, you\'ve felt more. Stories are like spiritual currency.”', 29),
  ('“The trouble is that we have a bad habit, encouraged by pedants and sophisticates, of considering happiness as something rather stupid. Only pain is intellectual, only evil interesting. This is the treason of the artist; a refusal to admit the banality of evil and the terrible boredom of pain.”', 27),
  ('“The truth is rarely pure and never simple.”', 23),
  ('“There are so many fragile things, after all. People break so easily, and so do dreams and hearts.”', 7),
  ('“There isn\'t a way things should be. There\'s just what happens, and what we do.”', 1),
  ('“There\'s always a story. It\'s all stories, really. The sun coming up every day is a story. Everything\'s got a story in it. Change the story, change the world.”', 1),
  ('“Time and I have quarrelled. All hours are midnight now. I had a clock and a watch, but I destroyed them both. I could not bear the way they mocked me.”', 10),
  ('“We do what we do, because of who we are. If we did otherwise, we would not be ourselves.”', 29),
  ('“We make choices. No one else can live our lives for us. And we must confront and accept the consequences of our actions.”', 29),
  ('“Why do you go away? So that you can come back. So that you can see the place you came from with new eyes and extra colors. And the people there see you differently, too. Coming back to where you started is not the same as never leaving.”', 1),
  ('“Will you, or will you not, quit me?\' I now demanded in a sudden passion, advancing close to him. \'I would prefer not to quit you\', he replied, gently emphasizing the not.”', 2),
  ('“Words save our lives, sometimes.”', 29),
  ('“You get what anybody gets - you get a lifetime.”', 29);
