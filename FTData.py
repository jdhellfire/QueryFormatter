TestData = \
    {

        'REPLACE_DISH': [{'INPUT': 'HellO-World', 'EXPECT': 'hello\\-world'},
                         {'INPUT': 'HellO-World-', 'EXPECT': 'hello\\-world\\-'}],

        'NO_REPLACE_DISH': [{'INPUT': "\"HellO-World\"", 'EXPECT': "\"hello-world\""},
                            {'INPUT': "\"HellO-World-\"", 'EXPECT': "\"hello-world-\""}]

    }
