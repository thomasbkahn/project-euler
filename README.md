# project-euler
Solutions to problems from [Project Euler](https://projecteuler.net/) in:
1. Python
2. C++
3. Julia
4. Octave/MATLAB

Each folder contains the solutions, as well as a README file that discusses the approach and the background mathematical theory, as well as the unique language-specific features that are being leveraged. The answer to each problem is calculated by a function that is always named `solution`, which is made to be as general as possible using parameter arguments. The default arguments reflect the specific values stated in the problem. All solutions use only the standard library of that language (except when an external library is absolutely necessary) and are intended to be as idiomatic as possible.

## Available Solutions

For all posted solutions, the amount of time that it takes to run (on my machine) is posted in the table below. A blank entry means that I haven't yet posted a solution for that problem in that language. "Closed form" in the Notes column means that a closed form solution is possible. In these cases, the closed form solution is discussed in the README, but the programmatic solutions ignore this option to provide more of a challenge.

|Number|Python|C++|Julia|MATLAB|Notes|
|---|---|---|---|---|---|
|001|33.6 µs||||Closed form|

## Timing Specs

Solutions are timed via repeatedly calling the `solution` function and averaging. The number of iterations is set such that the total time is about 10 seconds, though a minimum of three iterations is enforced for slow solutions. This algorithm is included in each solution file.

MATLAB code is executed with GNU Octave. C++ code is compiled with g++.

The specifications of my hardware and software (*i.e.* version numbers) are as follows:

|Component|Specification|
|---|---|
|Model|MacBook Pro (15 inch, Late 2011)|
|OS|OS X 10.11.3|
|CPU|2.5 GHz Intel Core i7|
|Memory|8 GB 1333 MHz DDR3|
|Python|3.5.1|
|g++|Apple LLVM version 7.0.2 (clang-700.1.81)|
|Julia|0.4.3|
|Octave|4.0.0|



## Should I be Posting These?
Technically, no. Quoting from the [Project Euler FAQ](https://projecteuler.net/):

> *I learned so much solving problem XXX so is it okay to publish my solution elsewhere?*
>
> It appears that you have answered your own question. There is nothing quite like that "Aha!" moment when you finally beat a problem which you have been working on for some time. It is often through the best of intentions in wishing to share our insights so that others can enjoy that moment too. Sadly, however, that will not be the case for your readers. Real learning is an active process and seeing how it is done is a long way from experiencing that epiphany of discovery. Please do not deny others what you have so richly valued yourself.

I can confirm the above statement. I have learned a ton from working through these problems, and I encourage anyone that has interest in these problems to attempt to solve them on your own before looking at my solutions.

I'm posting these solutions because:
1. This is far from the only place on the internet that you can find Project Euler solutions (and far from the most complete set). In fact, there are several GitHub repositories of Project Euler solutions.
2. In my opinion, the decision to "cheat" by looking at solutions is yours to make. If you are willing to work through these problems on your own first, you will most likely learn more than going through someone else's code. But if you just want to see an answer without going through the exercise, that's OK too.
3. After solving a problem, it is very helpful to go through other peoples solutions and see where you can improve your code. In this repository, I'll post solutions in several different languages, along with performance benchmarks. Hopefully this will be useful not only for building skills in your language of choice, but will also illustrate the different strengths of each language and help guide you in choosing tools for a certain task.
