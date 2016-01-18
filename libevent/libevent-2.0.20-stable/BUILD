cc_library(
    name = 'libevent-2.0.20-stable',
    srcs = [
        'event.c',
        'evthread.c',
        'buffer.c',
        'bufferevent.c',
        'bufferevent_sock.c',
        'bufferevent_filter.c',
        'bufferevent_pair.c',
        'listener.c',
        'bufferevent_ratelim.c',
        'evmap.c',
        'log.c',
        'evutil.c',
        'evutil_rand.c',
        'strlcpy.c',
        'select.c',
        'poll.c',
        'epoll.c',
        'signal.c',
        'event_tagging.c',
        'http.c',
        'evdns.c',
        'evrpc.c',
        'evthread_pthread.c',
        'bufferevent_openssl.c'
    ],
    deps = '#rt',
    incs = ['include', 'compat'],
    export_incs = 'include',
    defs = 'HAVE_CONFIG_H'
)

