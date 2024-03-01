## -- Exercice 1 -- ##

class Exercice1:
    def list_copy(l):
        lbis, lter = l, l[:]
        return id(l), id(lbis), id(lter), type(l)

    def elimulti(l):
        new = []
        for i in l:
            if not i in new:
                new.append(i)
        return new

## -- Exercice 2 -- ##

class Exercice2:
    def __init__(self, matrix):
        self.matrix = matrix
        self.lines = len(matrix)
        self.coeff = len(matrix[0]) - 1

    def exchange(self, l1, l2):
        self.matrix[l1], self.matrix[l2] = self.matrix[l2], self.matrix[l1]

    def multiply(self, r, l1):
        self.matrix[l1] = [a*r for a in self.matrix[l1]]

    def add(self, r, l1, l2):
        self.matrix[l1] = [a1 + a2*r for a1, a2 in zip(self.matrix[l1], self.matrix[l2])]

    def scale(self):
        for i in range(self.coeff):
            for j in range(i, self.lines):
                if self.matrix[j][i] != 0:
                    if i != j:
                        self.exchange(j, i)
                    for k in range(i + 1, self.lines):
                        a = self.matrix[k][i]
                        self.multiply(self.matrix[i][i], k)
                        self.add(-a, k, i)

    def solve(self):
        solutions = [self.matrix[-1][-1] / self.matrix[-1][-2]]
        for i in range(self.lines - 1):
            x = self.matrix[self.lines - i - 2][self.coeff]
            for j in range(self.lines - i - 1, self.coeff):
                x -= self.matrix[self.lines - i - 2][j]*solutions[self.lines - i - 1 - j]
            x /= self.matrix[self.lines - i - 2][self.lines - i - 2]
            solutions = [x] + solutions
        return solutions

    def show(self):
        print(self.matrix)

## -- Exercice 3 -- ##

class Exercice3:
    def phi(n):
        k = 0
        while n % 2 == 0:
            n //= 2
            k += 1
        j = (n - 1) // 2
        return (j, k)

    def encode(n):
        if n == 0:
            return 0
        elif n == 1:
            return (0, 0)
        j, k = phi(n)
        return (encode(j), encode(k))

    def decode(psy):
        if psy == 0:
            return 0
        elif psy == (0, 0):
            return 1
        j, k = psy
        return (decode(j) * 2 + 1) * 2 ** decode(k)

## -- Exercice 4 -- ##

class Exercice4:
    def encode(n, base):
        return [(n // base ** i) % base for i in range(8) if base ** i <= n][::-1]

    def decode(digits, base):
        return sum(v * (base ** k) for k, v in enumerate(digits[::-1]))

    def curious():
        return [2**i for i in range(20) if all(Exercice4.encode(2**i, 3))]

## -- Exercice 5 -- ##

class Exercice5:
    #   pr(x, n) => Exponentiation de x par n
    def pr(x, n):
        y, t = 1, []
        while n > 0:
            n, r = divmod(n, 2)
            t.insert(0, r)
        for b in t:
            y *= y
            if b:
                y *= x
        return y

    # dmd(a, b) => Divmod de a par b
    def dmd(a, b):
        assert b > 0 and a >= 0
        k, q = 0, 0
        while b <= a:
            k, b = k + 1, b * 2
        for j in range(k):
            b //= 2
            if b <= a:
                q, a = q * 2 + 1, a - b
            else:
                q *= 2
        return q, a

## -- Exercice 6 -- ##

class Exercice6:
    def pgcd(a, b):
        return pgcd(b, a % b) if a % b != 0 else b

## -- Exercice 7 -- ##

class Exercice7:
    def bezout(a, b):
        if b == 0:
            return (a, 1, 0)
        d, u, v = Exercice7.bezout(b, a % b)
        return (d, v, u - (a // b) * v)

## -- Exercice 8 -- ##

class Exercice8:
    prems = [2, 3, 5]

    def premier(n):
        i = 1
        while Exercice8.prems[-1] < n:
            for j in (-1, 1):
                if all((6 * i + j) % p != 0 for p in Exercice8.prems):
                    Exercice8.prems.append(6 * i + j)
            i += 1
        return n in Exercice8.prems

    def pdp(n):
        if Exercice8.premier(n):
            return n
        for p in Exercice8.prems:
            if n % p == 0:
                return p

    def pfp(n):
        res = []
        while n > 1:
            p, q = Exercice8.pdp(n), 1
            n //= p
            while Exercice8.pdp(n) == p:
                n, q = n // p, q + 1
            res.append([p, q])
        return res

## -- Exercice 9 -- ##

class Exercice9:
    def fact(n):
        return 1 if n == 1 else n * fact(n - 1)

    def binom(n, k):
        return fact(n) // (fact(k) - fact(n - k))

    def combin(n, k):
        res = []
        for _ in range(binom(n, k)):
            skip = []
            for __ in range(n - k):
                for a in range(n):
                    if not a in skip:
                        skip.append(a)
                        break
            liste = []
            for i in range(n):
                if not i in skip:
                    liste.append(i)
            res.append(liste)

        return res

if __name__ == "__main__":

    ## -- Exercice 2 -- ##

    sys = Exercice2([[0, 0, 0, 1, 1], [1, 1, 1, 1, 2], [8, 4, 2, 1, 9], [27, 9, 3, 1, 28]])
    sys.show()
    sys.scale()
    sys.show()
    print(sys.solve())