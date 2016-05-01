# 2016.05.01 15:28:21 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/symbol.py
"""Non-terminal symbols of Python grammar (from "graminit.h")."""
single_input = 256
file_input = 257
eval_input = 258
decorator = 259
decorators = 260
decorated = 261
funcdef = 262
parameters = 263
varargslist = 264
fpdef = 265
fplist = 266
stmt = 267
simple_stmt = 268
small_stmt = 269
expr_stmt = 270
augassign = 271
print_stmt = 272
del_stmt = 273
pass_stmt = 274
flow_stmt = 275
break_stmt = 276
continue_stmt = 277
return_stmt = 278
yield_stmt = 279
raise_stmt = 280
import_stmt = 281
import_name = 282
import_from = 283
import_as_name = 284
dotted_as_name = 285
import_as_names = 286
dotted_as_names = 287
dotted_name = 288
global_stmt = 289
exec_stmt = 290
assert_stmt = 291
compound_stmt = 292
if_stmt = 293
while_stmt = 294
for_stmt = 295
try_stmt = 296
with_stmt = 297
with_item = 298
except_clause = 299
suite = 300
testlist_safe = 301
old_test = 302
old_lambdef = 303
test = 304
or_test = 305
and_test = 306
not_test = 307
comparison = 308
comp_op = 309
expr = 310
xor_expr = 311
and_expr = 312
shift_expr = 313
arith_expr = 314
term = 315
factor = 316
power = 317
atom = 318
listmaker = 319
testlist_comp = 320
lambdef = 321
trailer = 322
subscriptlist = 323
subscript = 324
sliceop = 325
exprlist = 326
testlist = 327
dictorsetmaker = 328
classdef = 329
arglist = 330
argument = 331
list_iter = 332
list_for = 333
list_if = 334
comp_iter = 335
comp_for = 336
comp_if = 337
testlist1 = 338
encoding_decl = 339
yield_expr = 340
sym_name = {}
for _name, _value in globals().items():
    if type(_value) is type(0):
        sym_name[_value] = _name

def main():
    import sys
    import token
    if len(sys.argv) == 1:
        sys.argv = sys.argv + ['Include/graminit.h', 'Lib/symbol.py']
    token.main()


if __name__ == '__main__':
    main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\symbol.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:28:21 St�edn� Evropa (letn� �as)
