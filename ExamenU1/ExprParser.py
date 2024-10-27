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
        4,1,14,47,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,16,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,42,8,1,10,1,
        12,1,45,9,1,1,1,0,1,2,2,0,2,0,0,55,0,4,1,0,0,0,2,15,1,0,0,0,4,5,
        3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,6,1,-1,0,8,9,5,1,0,0,9,10,3,
        2,1,0,10,11,5,2,0,0,11,16,1,0,0,0,12,16,5,11,0,0,13,16,5,12,0,0,
        14,16,5,13,0,0,15,7,1,0,0,0,15,12,1,0,0,0,15,13,1,0,0,0,15,14,1,
        0,0,0,16,43,1,0,0,0,17,18,10,12,0,0,18,19,5,10,0,0,19,42,3,2,1,13,
        20,21,10,11,0,0,21,22,5,7,0,0,22,42,3,2,1,12,23,24,10,10,0,0,24,
        25,5,8,0,0,25,42,3,2,1,11,26,27,10,9,0,0,27,28,5,9,0,0,28,42,3,2,
        1,10,29,30,10,8,0,0,30,31,5,5,0,0,31,42,3,2,1,9,32,33,10,7,0,0,33,
        34,5,6,0,0,34,42,3,2,1,8,35,36,10,6,0,0,36,37,5,3,0,0,37,42,3,2,
        1,7,38,39,10,5,0,0,39,40,5,4,0,0,40,42,3,2,1,6,41,17,1,0,0,0,41,
        20,1,0,0,0,41,23,1,0,0,0,41,26,1,0,0,0,41,29,1,0,0,0,41,32,1,0,0,
        0,41,35,1,0,0,0,41,38,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,
        1,0,0,0,44,3,1,0,0,0,45,43,1,0,0,0,3,15,41,43
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'&&'", "'||'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "AND", "OR", 
                      "MAS", "MENOS", "MULT", "DIV", "MOD", "POW", "NUM", 
                      "BOOL", "VAR", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    AND=3
    OR=4
    MAS=5
    MENOS=6
    MULT=7
    DIV=8
    MOD=9
    POW=10
    NUM=11
    BOOL=12
    VAR=13
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

        def POW(self):
            return self.getToken(ExprParser.POW, 0)

        def MULT(self):
            return self.getToken(ExprParser.MULT, 0)

        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)

        def MOD(self):
            return self.getToken(ExprParser.MOD, 0)

        def MAS(self):
            return self.getToken(ExprParser.MAS, 0)

        def MENOS(self):
            return self.getToken(ExprParser.MENOS, 0)

        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

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
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 8
                self.match(ExprParser.T__0)
                self.state = 9
                self.expr(0)
                self.state = 10
                self.match(ExprParser.T__1)
                pass
            elif token in [11]:
                self.state = 12
                self.match(ExprParser.NUM)
                pass
            elif token in [12]:
                self.state = 13
                self.match(ExprParser.BOOL)
                pass
            elif token in [13]:
                self.state = 14
                self.match(ExprParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 41
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 18
                        self.match(ExprParser.POW)
                        self.state = 19
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 21
                        self.match(ExprParser.MULT)
                        self.state = 22
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 24
                        self.match(ExprParser.DIV)
                        self.state = 25
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 27
                        self.match(ExprParser.MOD)
                        self.state = 28
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 30
                        self.match(ExprParser.MAS)
                        self.state = 31
                        self.expr(9)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 33
                        self.match(ExprParser.MENOS)
                        self.state = 34
                        self.expr(8)
                        pass

                    elif la_ == 7:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 36
                        self.match(ExprParser.AND)
                        self.state = 37
                        self.expr(7)
                        pass

                    elif la_ == 8:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 39
                        self.match(ExprParser.OR)
                        self.state = 40
                        self.expr(6)
                        pass

             
                self.state = 45
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
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         




