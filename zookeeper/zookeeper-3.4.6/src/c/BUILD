cc_library(
    name = 'zookeeper-3.4.6',
    srcs = [
        'src/mt_adaptor.c',
        'src/recordio.c',
        'src/zk_hashtable.c',
        'src/zk_log.c',
        'src/zookeeper.c',
        'src/hashtable/hashtable.c',
        'src/hashtable/hashtable_itr.c',
        'generated/zookeeper.jute.c'
    ],
    incs = [
        '.',
        './include',
        './generated'
    ],
    defs = [
        'THREADED',
    ],
    extra_cppflags = [
        '-Wno-unused-variable',
        '-Wno-sign-compare'
    ],
    warning = []
)

cc_binary(
    name = 'zkCli',
    srcs = [
        'src/cli.c'
    ],
    incs = [
        '.',
        './include',
        './generated'
    ],
    defs = [
        'THREADED',
    ],
    deps = [
        ':zookeeper-3.4.6',
        '#pthread'
    ]

)
