male(princePhillip).

male(princeCharles).
male(captainMarkPhillips).
male(timothyLaurence).
male(princeAndrew).
male(princeEdward).

male(princeWilliam).
male(princeHarry).
male(peterPhillips).
male(mikeTindall).
male(jamesViscountSevern).

male(princeGeorge).


female(queenElizabethII).

female(princessDiana).
female(camillaParkerBowles).
female(princessAnne).
female(serahFerguson).
female(sophieRhysJones).

female(kateMiddleton).
female(autumnKelly).
female(zaraPhillips).
female(princessBeatrice).
female(princessEugenie).
female(ladyLouiseMountbattenWindsor).

female(princessCharlotte).
female(savannahPhillips).
female(islaPhillips).
female(miaGraceTindall).


married(princePhillip, queenElizabethII).
married(princeCharles, camillaParkerBowles).
married(timothyLaurence, princessAnne).
married(princeEdward, sophieRhysJones).
married(princeWilliam, kateMiddleton).
married(peterPhillips, autumnKelly).
married(mikeTindall, zaraPhillips).


divorced(princeCharles, princessDiana).
divorced(captainMarkPhillips, princessAnne).
divorced(princeAndrew, serahFerguson).

parent(princePhillip, princeCharles).
parent(queenElizabethII, princeCharles).
parent(princePhillip, princessAnne).
parent(queenElizabethII, princessAnne).
parent(princePhillip, princeAndrew).
parent(queenElizabethII, princeAndrew).
parent(princePhillip, princeEdward).
parent(queenElizabethII, princeEdward).

parent(princeCharles, princeWilliam).
parent(princessDiana,princeWilliam).
parent(princeCharles, princeHarry).
parent(princessDiana, princeHarry).

parent(captainMarkPhillips, peterPhillips).
parent(princessAnne, peterPhillips).
parent(captainMarkPhillips, zaraPhillips).
parent(princessAnne, zaraPhillips).

parent(princeAndrew, princessBeatrice).
parent(serahFerguson, princessBeatrice).
parent(princeAndrew, princessEugenie).
parent(serahFerguson, princessEugenie).

parent(princeEdward, jamesViscountSevern).
parent(sophieRhysJones, jamesViscountSevern).
parent(princeEdward, ladyLouiseMountbattenWindsor).
parent(sophieRhysJones, ladyLouiseMountbattenWindsor).

parent(princeWilliam, princeGeorge).
parent(kateMiddleton, princeGeorge).
parent(princeWilliam, princessCharlotte).
parent(kateMiddleton, princessCharlotte).

parent(peterPhillips, savannahPhillips).
parent(autumnKelly, savannahPhillips).
parent(peterPhillips, islaPhillips).
parent(autumnKelly, islaPhillips).

parent(mikeTindall, miaGraceTindall).
parent(zaraPhillips, miaGraceTindall).


husband(Person,Wife) :- married(Person,Wife).
wife(Person,Husband) :- married(Husband,Person).
father(Parent,Child) :- parent(Parent, Child), male(Parent).
mother(Parent,Child) :- parent(Parent, Child), female(Parent).
child(Child,Parent) :- parent(Parent, Child).
son(Child,Parent):- child(Child, Parent), male(Child).
daughter(Child,Parent):- child(Child, Parent), female(Child).

grandparent(GP,GC) :- parent(GP, A), parent(A, GC).
grandmother(GM,GC) :- grandparent(GM, GC), female(GM).
grandfather(GF,GC) :- grandparent(GF,GC), male(GF).
grandchild(GC,GP) :- grandparent(GP, GC).
grandson(GS,GP) :- grandchild(GS,GP), male(GS).
granddaughter(GD,GP) :- grandchild(GD,GP), female(GD).


sibling(Person1,Person2) :- father(Father, Person1), father(Father, Person2), mother(Mother, Person1), mother(Mother, Person2).
brother(Person,Sibling) :- sibling(Person, Sibling), male(Person).
sister(Person,Sibling) :- sibling(Person, Sibling), female(Person).
aunt(Person,NieceNephew) :- parent(A,NieceNephew), sister(Person,A).
uncle(Person,NieceNephew) :- parent(A,NieceNephew), brother(Person,A).
niece(Person,AuntUncle):- parent(A, Person), sibling(A, AuntUncle),female(Person).
nephew(Person,AuntUncle):-parent(A, Person), sibling(A, AuntUncle),male(Person).






