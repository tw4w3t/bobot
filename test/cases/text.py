"Testcases for text messages"

import re

from . import Case
from bobot.Rule import Rule

simpleText = Case.Case([
    Rule({
        'match': 'test',
        'response': 'test-yourself'
    }),
    Rule({
        'match': 'tost',
        'response': 'tost-yourself'
    }),
], [
    {
        'expected': [Case.Expectation('test-yourself').value()],
        'message': Case.Message('test').value()
    },
    {
        'expected': [Case.Expectation('tost-yourself').value()],
        'message': Case.Message('tost').value()
    }
])

regexText = Case.Case([
    Rule({
        'match': re.compile('test'),
        'response': 'inside had test'
    }),
    Rule({
        'match': re.compile('^test'),
        'response': 'starts with test'
    })
], [
    {
        'expected': [
            Case.Expectation('inside had test').value(),
            Case.Expectation('starts with test').value()
        ],
        'message': Case.Message('test dudu').value()
    }
])

arrayTextOr = Case.Case([
    Rule({
        'match': ['alpha', 'betta'],
        'response': 'alpha or betta'
    }),
    Rule({
        'match': ['alpha', 'gamma'],
        'response': 'alpha or gamma'
    })
], [
    {
        'expected': [Case.Expectation('alpha or betta').value()],
        'message': Case.Message('betta').value()
    },
    {
        'expected': [Case.Expectation('alpha or gamma').value()],
        'message': Case.Message('gamma').value()
    },
    {
        'expected': [
            Case.Expectation('alpha or betta').value(),
            Case.Expectation('alpha or gamma').value()
        ],
        'message': Case.Message('alpha').value()
    }
])

arrayTextAnd = Case.Case([
    Rule({
        'match': Rule.all(re.compile(r'^a'), re.compile(r'.+b$')),
        'response': 'starts from a, ends from b'
    }),
    Rule({
        'match': Rule.all(re.compile(r'^a'), re.compile(r'.+c$')),
        'response': 'starts from a, ends from c'
    })
], [
    {
        'expected': [],
        'message': Case.Message('test').value()
    },
    {
        'expected': [Case.Expectation('starts from a, ends from b').value()],
        'message': Case.Message('amb').value()
    },
    {
        'expected': [Case.Expectation('starts from a, ends from c').value()],
        'message': Case.Message('amc').value()
    },
])
