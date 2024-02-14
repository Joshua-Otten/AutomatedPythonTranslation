# This file helps create files of term lists to translate
# terms go below, separated by spaces
# code will format and eliminate duplicates

# ex: terms can be written like this:
#       'seed()   Initialize the random number generator'
# Or this:
#       'seed(arg)'
# Or simply:
#       'seed'

# test with random module
terms = '''

seed()    Initialize the random number generator
getstate()    Returns the current internal state of the random number generator
setstate()    Restores the internal state of the random number generator
getrandbits()    Returns a number representing the random bits
randrange()    Returns a random number between the given range
randint()    Returns a random number between the given range
choice()    Returns a random element from the given sequence
choices()    Returns a list with a random selection from the given sequence
shuffle()    Takes a sequence and returns the sequence in a random order
sample()    Returns a given sample of a sequence
random()    Returns a random float number between 0 and 1
uniform()    Returns a random float number between two given parameters
triangular()    Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
betavariate()    Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
expovariate()    Returns a random float number based on the Exponential distribution (used in statistics)
gammavariate()    Returns a random float number based on the Gamma distribution (used in statistics)
gauss()    Returns a random float number based on the Gaussian distribution (used in probability theories)
lognormvariate()    Returns a random float number based on a log-normal distribution (used in probability theories)
normalvariate()    Returns a random float number based on the normal distribution (used in probability theories)
vonmisesvariate()    Returns a random float number based on the von Mises distribution (used in directional statistics)
paretovariate()    Returns a random float number based on the Pareto distribution (used in probability theories)
weibullvariate()    Returns a random float number based on the Weibull distribution (used in statistics)

'''


# (from numpy)
'''
all()
any()
take()
put()
apply_along_axis()
apply_over_axes()
argmin()
argmax()
nanargmin()
nanargmax()
amax()
amin()
insert()
delete()
append()
around()
flip()
fliplr()
flipud()
triu()
tril()
tri()
empty()
empty_like()
zeros()
zeros_like()
ones()
ones_like()
full_like()
diag()
diagflat()
diag_indices()
asmatrix()
bmat()
eye()
roll()
identity()
arange()
place()
extract()
compress()
rot90()
tile()
reshape()
ravel()
isinf()
isrealobj()
isscalar()
isneginf()
isposinf()
iscomplex()
isnan()
iscomplexobj()
isreal()
isfinite()
isfortran()
exp()
exp2()
fix()
hypot()
absolute()
ceil()
floor()
degrees()
radians()
npv()
fv()
pv()
power()
float_power()
log()
log1()
log2()
log10()
dot()
vdot()
trunc()
divide()
floor_divide()
true_divide()
random.rand()
random.randn()
ndarray.flat()
expm1()
bincount()
rint()
equal()
not_equal()
less()
less_equal()
greater()
greater_equal()
prod()
square()
cbrt()
logical_or()
logical_and()
logical_not()
logical_xor()
array_equal()
array_equiv()
sin()
cos()
tan()
sinh()
cosh()
tanh()
arcsin()
arccos()
arctan()
arctan2()


all([axis, out, keepdims, where])
any([axis, out, keepdims, where])
argmax([axis, out, keepdims])
argmin([axis, out, keepdims])
argpartition(kth[, axis, kind, order])
argsort([axis, kind, order])
astype(dtype[, order, casting, subok, copy])
byteswap([inplace])
choose(choices[, out, mode])
clip([min, max, out])
compress(condition[, axis, out])
conj()
conjugate()
copy([order])
cumprod([axis, dtype, out])
cumsum([axis, dtype, out])
diagonal([offset, axis1, axis2])
dump(file)
dumps()
fill(value)
flatten([order])
getfield(dtype[, offset])
item(*args)
itemset(*args)
max([axis, out, keepdims, initial, where])
mean([axis, dtype, out, keepdims, where])
min([axis, out, keepdims, initial, where])
newbyteorder([new_order])
nonzero()
partition(kth[, axis, kind, order])
prod([axis, dtype, out, keepdims, initial, ...])
ptp([axis, out, keepdims])
put(indices, values[, mode])
ravel([order])
repeat(repeats[, axis])
reshape(shape[, order])
resize(new_shape[, refcheck])
round([decimals, out])
searchsorted(v[, side, sorter])
setfield(val, dtype[, offset])
setflags([write, align, uic])
sort([axis, kind, order])
squeeze([axis])
std([axis, dtype, out, ddof, keepdims, where])
sum([axis, dtype, out, keepdims, initial, where])
swapaxes(axis1, axis2)
take(indices[, axis, out, mode])
tobytes([order])
tofile(fid[, sep, format])
tolist()
tostring([order])
trace([offset, axis1, axis2, dtype, out])
transpose(*axes)
var([axis, dtype, out, ddof, keepdims, where])
view([dtype][, type])
'''

# read in all currently known terms
f = open('already_known_terms.txt','r')
known = f.readlines()
f.close()
for i in range(len(known)):
    known[i] = known[i].strip()

s = set()

split_terms = terms.split('\n')
for term in split_terms:
    if term != '' and term.strip() not in known:
        to_add = term.split()[0].strip() # want first element in line
        #if to_add[len(to_add)-2:len(to_add)] == "()":
        #    to_add = to_add[:len(to_add)-2]

        if '(' in to_add:
            # get rid of all parentheticals + stuff inside
            to_add = to_add[:to_add.index('(')]

        if to_add not in known:
            s.add(to_add)


# writing to a file
n = open('to_expand.txt','w')
for term in s:
    n.write(term+'\n')
n.close()
