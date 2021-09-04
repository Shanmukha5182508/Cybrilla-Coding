T = int(input())

while T > 0:

  N, K = list(map(int, input().split(" ")))

  arr = list(map(int, input().split(" ")))

  arr = [i for i in arr if i > 0]

  if len(arr) == 0:

    print(0)

  elif len(arr) == 1:

    print(arr[0])

  else:

    if K == 1:

      print(max(arr))

    elif (K >= len(arr)):

      print(sum(arr))

    else:

      ctr = Counter(arr)

      res = []

      for k,v in ctr.items():

        res.append(k*v)

    print(sum(sorted(res, reverse=True)[:K]))

  T -= 1
