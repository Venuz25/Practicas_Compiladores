# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,56,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,5,1,51,8,1,10,1,12,1,54,9,1,1,1,0,1,2,2,0,2,
        0,0,65,0,4,1,0,0,0,2,19,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,
        0,0,7,8,6,1,-1,0,8,9,5,11,0,0,9,10,3,2,1,0,10,11,5,12,0,0,11,12,
        3,2,1,7,12,20,1,0,0,0,13,14,5,11,0,0,14,15,3,2,1,0,15,16,5,12,0,
        0,16,20,1,0,0,0,17,20,5,3,0,0,18,20,5,4,0,0,19,7,1,0,0,0,19,13,1,
        0,0,0,19,17,1,0,0,0,19,18,1,0,0,0,20,52,1,0,0,0,21,22,10,13,0,0,
        22,23,5,5,0,0,23,51,3,2,1,14,24,25,10,12,0,0,25,26,5,6,0,0,26,51,
        3,2,1,13,27,28,10,11,0,0,28,29,5,7,0,0,29,51,3,2,1,12,30,31,10,10,
        0,0,31,32,5,8,0,0,32,51,3,2,1,11,33,34,10,9,0,0,34,35,5,10,0,0,35,
        51,3,2,1,10,36,37,10,8,0,0,37,38,5,9,0,0,38,51,3,2,1,9,39,40,10,
        4,0,0,40,41,5,1,0,0,41,51,3,2,1,5,42,43,10,3,0,0,43,44,5,2,0,0,44,
        51,3,2,1,4,45,46,10,6,0,0,46,47,5,11,0,0,47,48,3,2,1,0,48,49,5,12,
        0,0,49,51,1,0,0,0,50,21,1,0,0,0,50,24,1,0,0,0,50,27,1,0,0,0,50,30,
        1,0,0,0,50,33,1,0,0,0,50,36,1,0,0,0,50,39,1,0,0,0,50,42,1,0,0,0,
        50,45,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,3,1,0,
        0,0,54,52,1,0,0,0,3,19,50,52
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'&&'", "'||'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'('", "')'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NUM", "BOOL", "MAS", "MENOS", 
                      "MULT", "DIV", "MOD", "POW", "PAREI", "PARED", "EQ", 
                      "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NUM=3
    BOOL=4
    MAS=5
    MENOS=6
    MULT=7
    DIV=8
    MOD=9
    POW=10
    PAREI=11
    PARED=12
    EQ=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAREI(self):
            return self.getToken(ExprParser.PAREI, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def PARED(self):
            return self.getToken(ExprParser.PARED, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def MAS(self):
            return self.getToken(ExprParser.MAS, 0)

        def MENOS(self):
            return self.getToken(ExprParser.MENOS, 0)

        def MULT(self):
            return self.getToken(ExprParser.MULT, 0)

        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)

        def POW(self):
            return self.getToken(ExprParser.POW, 0)

        def MOD(self):
            return self.getToken(ExprParser.MOD, 0)

        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 8
                self.match(ExprParser.PAREI)
                self.state = 9
                self.expr(0)
                self.state = 10
                self.match(ExprParser.PARED)
                self.state = 11
                self.expr(7)
                pass

            elif la_ == 2:
                self.state = 13
                self.match(ExprParser.PAREI)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.match(ExprParser.PARED)
                pass

            elif la_ == 3:
                self.state = 17
                self.match(ExprParser.NUM)
                pass

            elif la_ == 4:
                self.state = 18
                self.match(ExprParser.BOOL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 22
                        self.match(ExprParser.MAS)
                        self.state = 23
                        self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 25
                        self.match(ExprParser.MENOS)
                        self.state = 26
                        self.expr(13)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 28
                        self.match(ExprParser.MULT)
                        self.state = 29
                        self.expr(12)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 31
                        self.match(ExprParser.DIV)
                        self.state = 32
                        self.expr(11)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 34
                        self.match(ExprParser.POW)
                        self.state = 35
                        self.expr(10)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 37
                        self.match(ExprParser.MOD)
                        self.state = 38
                        self.expr(9)
                        pass

                    elif la_ == 7:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 40
                        self.match(ExprParser.AND)
                        self.state = 41
                        self.expr(5)
                        pass

                    elif la_ == 8:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 43
                        self.match(ExprParser.OR)
                        self.state = 44
                        self.expr(4)
                        pass

                    elif la_ == 9:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 46
                        self.match(ExprParser.PAREI)
                        self.state = 47
                        self.expr(0)
                        self.state = 48
                        self.match(ExprParser.PARED)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         




