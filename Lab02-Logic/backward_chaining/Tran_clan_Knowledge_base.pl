#facts
nam(tranminhtong).
nam(hoquyly).
nam(hohanthuong).
nam(trannghetong).
nam(tranthuantong).
nam(giandinhde).
nam(tranquangde).
nam(tranthieude).
nam(trandutong).
nam(tranhientong).
nam(tranduetong).
nam(tranphede).
nam(cungtuc).
nam(duongnhatle).
nam(tranngac).


nu(hientu).
nu(huyninh).
nu(lethanhngau).
nu(thuctu).
nu(giatu).
nu(vuongmau).

vochong(tranminhtong, hientu).
vochong(hoquyly, huyninh).
vochong(tranthuantong, lethanhngau).
vochong(tranduetong, giatu).
vochong(cungtuc, vuongmau).

cha(tranminhtong, huyninh).
cha(tranminhtong, trannghetong).
cha(tranminhtong, trandutong).
cha(tranminhtong, tranhientong).
cha(tranminhtong, tranduetong).
cha(tranminhtong, cungtuc).
cha(hoquyly, hohanthuong).
cha(hoquyly, lethanhngau).
cha(trannghetong, tranthuantong).
cha(trannghetong, tranngac).
cha(trannghetong, giandinhde).
cha(tranduetong, tranphede).
cha(cungtuc, duongnhatle).
cha(tranngac, tranquangde).
cha(tranthuantong, tranthieude).

me(hientu, huyninh).
me(hientu, trannghetong).
me(hientu, trandutong).
me(hientu, tranhientong).
me(hientu, tranduetong).
me(hientu, cungtuc).
me(huyninh, hohanthuong).
me(huyninh, lethanhngau).
me(thuctu, tranthuantong).
me(thuctu, tranngac).
me(thuctu, giandinhde).
me(giatu, tranphede).
me(vuongmau, duongnhatle).
me(lethanhngau, tranthieude).

anhtrai(tranhientong, trannghetong).
anhtrai(tranhientong, trandutong).
anhtrai(tranhientong, trannghetong).
anhtrai(tranhientong, cungtuc).
anhtrai(tranhientong, huyninh).
anhtrai(trannghetong, trandutong).
anhtrai(trannghetong, tranduetong).
anhtrai(trannghetong, cungtuc).
anhtrai(trannghetong, huyninh).
anhtrai(cungtuc, trandutong).
anhtrai(cungtuc, tranduetong).
anhtrai(cungtuc, huyninh).
anhtrai(trandutong, tranduetong).
anhtrai(trandutong, huyninh).
anhtrai(tranduetong, huyninh).

anhtrai(tranngac, tranthuantong).
anhtrai(tranngac, giandinhde).
anhtrai(giandinhde, tranthuantong).

vua(tranminhtong).
vua(trannghetong).
vua(hoquyly).
vua(trandutong).
vua(tranhientong).
vua(tranduetong).
vua(hohanthuong).
vua(tranthuantong).
vua(tranphede).
vua(duongnhatle).
vua(tranthieude).
vua(tranquangde).

	#rules
phuhuynh(Phuhuynh, Con):- cha(Phuhuynh, Con); me(Phuhuynh, Con).

con(Con, Nguoi):- cha(Nguoi, Con); me(Nguoi, Con).

contrai(Con, Nguoi):- cha(Nguoi, Con).

congai(Con, Nguoi):- me(Nguoi, Con).

anhemruot(ConA, ConB):-
    ((cha(X, ConA), cha(Y, ConB), X == Y);
    (me(Z, ConA), me(D, ConB), Z == D)).


chigai(Chi, Em):-
    anhemruot(Chi, Em),
    nu(Chi).

anhemho(ConA, ConB):-
    phuhuynh(PhA, ConA),
    phuhuynh(PhB, ConB),
    anhemruot(PhA, PhB).

ongba(OngBa, Chau):-
    phuhuynh(Ph, Chau),
    phuhuynh(OngBa, Ph).

ongbangoai(OngBa, Chau):-
    me(Me, Chau),
    phuhuynh(OngBa, Me).

ongbanoi(OngBa, Chau):-
    cha(Cha, Chau),
    phuhuynh(OngBa, Cha).

ongnoi(Ong, Chau):-
    cha(Cha, Chau),
    cha(Ong, Cha).

banoi(Ba, Chau):-
    cha(Cha, Chau),
    me(Ba, Cha).

ongngoai(Ong, Chau):-
    me(Me, Chau),
    cha(Ong, Me).

bangoai(Ba, Chau):-
    me(Me, Chau),
    me(Ba, Me).

chau(Chau, OngBa):-
    ongba(OngBa, Chau).

chaunoi(Chau, OngBa):-
    ongbanoi(OngBa, Chau).

chaungoai(Chau, OngBa):-
    ongbangoai(OngBa, Chau).

chu(Chu, Chau):-
    cha(Cha, Chau),
    anhtrai(Cha, Chu).

bac(Bac, Chau):-
    cha(Cha, Chau),
    anhtrai(Bac, Cha).

cau(Cau, Chau):-
    nam(Cau),
    me(Me, Chau),
    anhemruot(Me, Cau).

co(Co, Chau):-
    nu(Co),
    me(Me, Chau),
    anhemruot(Me, Co).

co(Co, Chau):-
    nu(Co),
    cha(Cha, Chau),
    anhtrai(Cha, Co).

hoanghau(Nguoi, Vua):-
    nu(Nguoi),
    vua(Vua),
    vochong(Vua, Nguoi).

hoangthaihau(Nguoi, Vua):-
    nu(Nguoi),
    me(Nguoi, Vua),
    vua(Vua),
    vochong(Chong, Nguoi),
    vua(Chong).

quocmau(Nguoi, Vua):-
    nu(Nguoi),
    me(Nguoi, Vua),
    vua(Vua),
    vochong(Chong, Nguoi),
    \+ vua(Chong).

quoclao(Nguoi, Vua):-
    nam(Nguoi),
    cha(Nguoi, Vua),
    vua(Vua),
    \+ vua(Nguoi).

thaithuonghoang(Nguoi, Vua):-
    nam(Nguoi),
    vua(Vua),
    cha(Nguoi, Vua),
    vua(Nguoi).

thaimau(Nguoi, Vua):-
    banoi(Nguoi, Vua),
    vua(Vua).

hoanghuynh(Nguoi, Vua):-
    vua(Vua),
    anhtrai(Nguoi, Vua).

hoangde(Nguoi, Vua):-
    nam(Nguoi),
    anhtrai(Vua, Nguoi),
    vua(Vua).

hoangty(Nguoi, Vua):-
    vua(Vua),
    chigai(Nguoi, Vua).

hoangmuoi(Nguoi, Vua):-
    vua(Vua),
    nu(Nguoi),
    anhtrai(Vua, Nguoi).

hoangtu(Nguoi, Vua):-
    nam(Nguoi),
    vua(Vua),
    cha(Vua, Nguoi).

thaitu(Nguoi, Vua):-
    nam(Nguoi),
    vua(Vua),
    cha(Vua, Nguoi),
    vua(Nguoi).

congchua(Nguoi, Vua):-
    nu(Nguoi),
    vua(Vua),
    cha(Vua, Nguoi).

hoangtuc(Nguoi, Vua):-
    vochong(HoangTu, Nguoi),
    hoangtu(HoangTu, Vua).

hoangphi(Nguoi, Vua):-
    vochong(ThaiTu, Nguoi),
    thaitu(ThaiTu, Vua).

phoma(Nguoi, Vua):-
    vochong(Nguoi, CongChua),
    congchua(CongChua, Vua).

phuhoang(Con, Vua):-
    cha(Vua, Con),
    vua(Vua).

hoangthuc(Nguoi, Vua):-
    chu(Nguoi, Vua),
    vua(Vua).

quoctruong(Nguoi, Vua):-
    vua(Vua),
    vochong(Vua, HoangHau),
    cha(Nguoi, HoangHau).

hoangba(Nguoi, Vua):-
    vua(Vua),
    bac(Nguoi, Vua).
