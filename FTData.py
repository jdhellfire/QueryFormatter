TestData = \
    {

        'REPLACE_DISH': [{'INPUT': "HellO-World", 'EXPECT': "hello\\-world"},
                         {'INPUT': "HellO-World-", 'EXPECT': "hello\\-world\\-"}],

        'NO_REPLACE_DISH': [{'INPUT': "\"HellO-World\"", 'EXPECT': "\"hello-world\""},
                            {'INPUT': "\"HellO-World-\"", 'EXPECT': "\"hello-world-\""}],
        "HAS_BEEN_REPLACED" :[{'INPUT': "hello\\-world", 'EXPECT': "hello\\-world"},
                              {'INPUT': "hello\\-world\\-", 'EXPECT': "hello\\-world\\-"}]

    }
