"""
heapq.nlargest(n, iterable, key=None)
Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a
function of one argument that is used to extract a comparison key from each element in iterable
(for example, key=str.lower). Equivalent to: sorted(iterable, key=key, reverse=True)[:n].
"""



def top10Actor():
    ActorMovie = [['Leonardo DiCaprio','The Revenant'],
                    ['Samuel L. Jackson','Pulp Fiction'],
                    ['Tom Cruise','Mission Impossible'],
                    ['Leonardo DiCaprio','The Great Gatsby'],
                  ['A', 'Mission Impossible'],
                  ['A', 'Mission Impossible'],
                  ['C', 'Mission Impossible'],
                  ['D', 'Mission Impossible'],
                  ['E', 'Mission Impossible'],
                  ['F', 'Mission Impossible'],
                  ['G', 'Mission Impossible'],
                  ['A', 'Mission Impossible'],
                  ['A', 'Mission Impossible'],
                  ['C', 'Mission Impossible'],
                  ['D', 'Mission Impossible'],
                  ['E', 'Mission Impossible'],
                  ['F', 'Mission Impossible'],
                  ['G', 'Mission Impossible'],
                  ['H', 'Mission Impossible']]
    actorMovieCount = {}
    for actor in ActorMovie:
        if actor[0] in actorMovieCount:
            actorMovieCount[actor[0]] += 1
        else:
            actorMovieCount[actor[0]] = 1
    actorMovieCount = dict(sorted(actorMovieCount.items(), key=lambda item: item[1],reverse=True))
    cnt = 0
    rank = 0
    for (key,val) in actorMovieCount.items():
        if rank != val:
            rank = val
            cnt += 1
        print("Actor Name: ",key,"**Count of movie** " , cnt)
        if cnt == 10:
            exit()


top10Actor()