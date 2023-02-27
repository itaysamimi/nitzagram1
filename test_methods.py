from classes.Comment import Comment
from classes.Post import Post


def test_comment():
    comment = Comment("This is your first comment")
    comment.display(0)


def test_post():
    new_post = Post("Images/ronaldo.jpg", "Home",
                    "Your post class is working!!!!!!")
    new_post.display()


