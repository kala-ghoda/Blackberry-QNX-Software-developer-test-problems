### Porting Python2.x code to Python3.8

Well, first of all the basic change I see in Python 2.x and Python3 are small functions, like print, divide, etc.
So I will use Futurize `future` module, as it provides support for backporting. I will then test with trial and error method for short code base, checking what points are giving error. For a larger tool base, it would be more efficient to use some tool for checking and taking a diff.
