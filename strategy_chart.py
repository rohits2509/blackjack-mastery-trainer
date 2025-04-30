# strategy_chart.py

HINTS = {
    # Hard totals
    ('hard', 8, 10): 'Hit',
    ('hard', 9, 3): 'Double',
    ('hard', 10, 9): 'Double',
    ('hard', 11, 6): 'Double',
    ('hard', 12, 4): 'Stand',
    ('hard', 13, 6): 'Stand',
    ('hard', 16, 10): 'Hit',
    ('hard', 17, 10): 'Stand',

    # Soft totals
    ('soft', 13, 5): 'Hit',
    ('soft', 15, 6): 'Double',
    ('soft', 17, 4): 'Double',
    ('soft', 18, 2): 'Stand',
    ('soft', 18, 7): 'Stand',
    ('soft', 18, 9): 'Hit',

    # Pairs
    ('pair', 2, 4): 'Split',
    ('pair', 6, 5): 'Split',
    ('pair', 8, 10): 'Split',
    ('pair', 9, 7): 'Stand',
    ('pair', 10, 6): 'Stand',
    ('pair', 5, 6): 'Double'
}
