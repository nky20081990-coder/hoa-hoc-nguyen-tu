import streamlit as st

st.set_page_config(
    page_title="Quantum → Nguyên tố",
    page_icon="⚛️",
    layout="wide"
)

# ============================================================
# DỮ LIỆU 118 NGUYÊN TỐ
# Z, symbol, name, period, group, category, electron_config
# ============================================================
ELEMENTS = [
(1,"H","Hydrogen",1,1,"Phi kim","1s1"),
(2,"He","Helium",1,18,"Khí hiếm","1s2"),
(3,"Li","Lithium",2,1,"Kim loại kiềm","1s2 2s1"),
(4,"Be","Beryllium",2,2,"Kim loại kiềm thổ","1s2 2s2"),
(5,"B","Boron",2,13,"Á kim","1s2 2s2 2p1"),
(6,"C","Carbon",2,14,"Phi kim","1s2 2s2 2p2"),
(7,"N","Nitrogen",2,15,"Phi kim","1s2 2s2 2p3"),
(8,"O","Oxygen",2,16,"Phi kim","1s2 2s2 2p4"),
(9,"F","Fluorine",2,17,"Halogen","1s2 2s2 2p5"),
(10,"Ne","Neon",2,18,"Khí hiếm","1s2 2s2 2p6"),
(11,"Na","Sodium",3,1,"Kim loại kiềm","1s2 2s2 2p6 3s1"),
(12,"Mg","Magnesium",3,2,"Kim loại kiềm thổ","1s2 2s2 2p6 3s2"),
(13,"Al","Aluminium",3,13,"Kim loại","1s2 2s2 2p6 3s2 3p1"),
(14,"Si","Silicon",3,14,"Á kim","1s2 2s2 2p6 3s2 3p2"),
(15,"P","Phosphorus",3,15,"Phi kim","1s2 2s2 2p6 3s2 3p3"),
(16,"S","Sulfur",3,16,"Phi kim","1s2 2s2 2p6 3s2 3p4"),
(17,"Cl","Chlorine",3,17,"Halogen","1s2 2s2 2p6 3s2 3p5"),
(18,"Ar","Argon",3,18,"Khí hiếm","1s2 2s2 2p6 3s2 3p6"),
(19,"K","Potassium",4,1,"Kim loại kiềm","[Ar] 4s1"),
(20,"Ca","Calcium",4,2,"Kim loại kiềm thổ","[Ar] 4s2"),
(21,"Sc","Scandium",4,3,"Kim loại chuyển tiếp","[Ar] 3d1 4s2"),
(22,"Ti","Titanium",4,4,"Kim loại chuyển tiếp","[Ar] 3d2 4s2"),
(23,"V","Vanadium",4,5,"Kim loại chuyển tiếp","[Ar] 3d3 4s2"),
(24,"Cr","Chromium",4,6,"Kim loại chuyển tiếp","[Ar] 3d5 4s1"),
(25,"Mn","Manganese",4,7,"Kim loại chuyển tiếp","[Ar] 3d5 4s2"),
(26,"Fe","Iron",4,8,"Kim loại chuyển tiếp","[Ar] 3d6 4s2"),
(27,"Co","Cobalt",4,9,"Kim loại chuyển tiếp","[Ar] 3d7 4s2"),
(28,"Ni","Nickel",4,10,"Kim loại chuyển tiếp","[Ar] 3d8 4s2"),
(29,"Cu","Copper",4,11,"Kim loại chuyển tiếp","[Ar] 3d10 4s1"),
(30,"Zn","Zinc",4,12,"Kim loại chuyển tiếp","[Ar] 3d10 4s2"),
(31,"Ga","Gallium",4,13,"Kim loại","[Ar] 3d10 4s2 4p1"),
(32,"Ge","Germanium",4,14,"Á kim","[Ar] 3d10 4s2 4p2"),
(33,"As","Arsenic",4,15,"Á kim","[Ar] 3d10 4s2 4p3"),
(34,"Se","Selenium",4,16,"Phi kim","[Ar] 3d10 4s2 4p4"),
(35,"Br","Bromine",4,17,"Halogen","[Ar] 3d10 4s2 4p5"),
(36,"Kr","Krypton",4,18,"Khí hiếm","[Ar] 3d10 4s2 4p6"),
(37,"Rb","Rubidium",5,1,"Kim loại kiềm","[Kr] 5s1"),
(38,"Sr","Strontium",5,2,"Kim loại kiềm thổ","[Kr] 5s2"),
(39,"Y","Yttrium",5,3,"Kim loại chuyển tiếp","[Kr] 4d1 5s2"),
(40,"Zr","Zirconium",5,4,"Kim loại chuyển tiếp","[Kr] 4d2 5s2"),
(41,"Nb","Niobium",5,5,"Kim loại chuyển tiếp","[Kr] 4d4 5s1"),
(42,"Mo","Molybdenum",5,6,"Kim loại chuyển tiếp","[Kr] 4d5 5s1"),
(43,"Tc","Technetium",5,7,"Kim loại chuyển tiếp","[Kr] 4d5 5s2"),
(44,"Ru","Ruthenium",5,8,"Kim loại chuyển tiếp","[Kr] 4d7 5s1"),
(45,"Rh","Rhodium",5,9,"Kim loại chuyển tiếp","[Kr] 4d8 5s1"),
(46,"Pd","Palladium",5,10,"Kim loại chuyển tiếp","[Kr] 4d10"),
(47,"Ag","Silver",5,11,"Kim loại chuyển tiếp","[Kr] 4d10 5s1"),
(48,"Cd","Cadmium",5,12,"Kim loại chuyển tiếp","[Kr] 4d10 5s2"),
(49,"In","Indium",5,13,"Kim loại","[Kr] 4d10 5s2 5p1"),
(50,"Sn","Tin",5,14,"Kim loại","[Kr] 4d10 5s2 5p2"),
(51,"Sb","Antimony",5,15,"Á kim","[Kr] 4d10 5s2 5p3"),
(52,"Te","Tellurium",5,16,"Á kim","[Kr] 4d10 5s2 5p4"),
(53,"I","Iodine",5,17,"Halogen","[Kr] 4d10 5s2 5p5"),
(54,"Xe","Xenon",5,18,"Khí hiếm","[Kr] 4d10 5s2 5p6"),
(55,"Cs","Cesium",6,1,"Kim loại kiềm","[Xe] 6s1"),
(56,"Ba","Barium",6,2,"Kim loại kiềm thổ","[Xe] 6s2"),
(57,"La","Lanthanum",6,3,"Lantan","[Xe] 5d1 6s2"),
(58,"Ce","Cerium",6,"—","Lantanide","[Xe] 4f1 5d1 6s2"),
(59,"Pr","Praseodymium",6,"—","Lantanide","[Xe] 4f3 6s2"),
(60,"Nd","Neodymium",6,"—","Lantanide","[Xe] 4f4 6s2"),
(61,"Pm","Promethium",6,"—","Lantanide","[Xe] 4f5 6s2"),
(62,"Sm","Samarium",6,"—","Lantanide","[Xe] 4f6 6s2"),
(63,"Eu","Europium",6,"—","Lantanide","[Xe] 4f7 6s2"),
(64,"Gd","Gadolinium",6,"—","Lantanide","[Xe] 4f7 5d1 6s2"),
(65,"Tb","Terbium",6,"—","Lantanide","[Xe] 4f9 6s2"),
(66,"Dy","Dysprosium",6,"—","Lantanide","[Xe] 4f10 6s2"),
(67,"Ho","Holmium",6,"—","Lantanide","[Xe] 4f11 6s2"),
(68,"Er","Erbium",6,"—","Lantanide","[Xe] 4f12 6s2"),
(69,"Tm","Thulium",6,"—","Lantanide","[Xe] 4f13 6s2"),
(70,"Yb","Ytterbium",6,"—","Lantanide","[Xe] 4f14 6s2"),
(71,"Lu","Lutetium",6,3,"Lantanide","[Xe] 4f14 5d1 6s2"),
(72,"Hf","Hafnium",6,4,"Kim loại chuyển tiếp","[Xe] 4f14 5d2 6s2"),
(73,"Ta","Tantalum",6,5,"Kim loại chuyển tiếp","[Xe] 4f14 5d3 6s2"),
(74,"W","Tungsten",6,6,"Kim loại chuyển tiếp","[Xe] 4f14 5d4 6s2"),
(75,"Re","Rhenium",6,7,"Kim loại chuyển tiếp","[Xe] 4f14 5d5 6s2"),
(76,"Os","Osmium",6,8,"Kim loại chuyển tiếp","[Xe] 4f14 5d6 6s2"),
(77,"Ir","Iridium",6,9,"Kim loại chuyển tiếp","[Xe] 4f14 5d7 6s2"),
(78,"Pt","Platinum",6,10,"Kim loại chuyển tiếp","[Xe] 4f14 5d9 6s1"),
(79,"Au","Gold",6,11,"Kim loại chuyển tiếp","[Xe] 4f14 5d10 6s1"),
(80,"Hg","Mercury",6,12,"Kim loại chuyển tiếp","[Xe] 4f14 5d10 6s2"),
(81,"Tl","Thallium",6,13,"Kim loại","[Xe] 4f14 5d10 6s2 6p1"),
(82,"Pb","Lead",6,14,"Kim loại","[Xe] 4f14 5d10 6s2 6p2"),
(83,"Bi","Bismuth",6,15,"Kim loại","[Xe] 4f14 5d10 6s2 6p3"),
(84,"Po","Polonium",6,16,"Kim loại","[Xe] 4f14 5d10 6s2 6p4"),
(85,"At","Astatine",6,17,"Halogen","[Xe] 4f14 5d10 6s2 6p5"),
(86,"Rn","Radon",6,18,"Khí hiếm","[Xe] 4f14 5d10 6s2 6p6"),
(87,"Fr","Francium",7,1,"Kim loại kiềm","[Rn] 7s1"),
(88,"Ra","Radium",7,2,"Kim loại kiềm thổ","[Rn] 7s2"),
(89,"Ac","Actinium",7,3,"Actinide","[Rn] 6d1 7s2"),
(90,"Th","Thorium",7,"—","Actinide","[Rn] 6d2 7s2"),
(91,"Pa","Protactinium",7,"—","Actinide","[Rn] 5f2 6d1 7s2"),
(92,"U","Uranium",7,"—","Actinide","[Rn] 5f3 6d1 7s2"),
(93,"Np","Neptunium",7,"—","Actinide","[Rn] 5f4 6d1 7s2"),
(94,"Pu","Plutonium",7,"—","Actinide","[Rn] 5f6 7s2"),
(95,"Am","Americium",7,"—","Actinide","[Rn] 5f7 7s2"),
(96,"Cm","Curium",7,"—","Actinide","[Rn] 5f7 6d1 7s2"),
(97,"Bk","Berkelium",7,"—","Actinide","[Rn] 5f9 7s2"),
(98,"Cf","Californium",7,"—","Actinide","[Rn] 5f10 7s2"),
(99,"Es","Einsteinium",7,"—","Actinide","[Rn] 5f11 7s2"),
(100,"Fm","Fermium",7,"—","Actinide","[Rn] 5f12 7s2"),
(101,"Md","Mendelevium",7,"—","Actinide","[Rn] 5f13 7s2"),
(102,"No","Nobelium",7,"—","Actinide","[Rn] 5f14 7s2"),
(103,"Lr","Lawrencium",7,3,"Actinide","[Rn] 5f14 7s2 7p1"),
(104,"Rf","Rutherfordium",7,4,"Kim loại chuyển tiếp","[Rn] 5f14 6d2 7s2"),
(105,"Db","Dubnium",7,5,"Kim loại chuyển tiếp","[Rn] 5f14 6d3 7s2"),
(106,"Sg","Seaborgium",7,6,"Kim loại chuyển tiếp","[Rn] 5f14 6d4 7s2"),
(107,"Bh","Bohrium",7,7,"Kim loại chuyển tiếp","[Rn] 5f14 6d5 7s2"),
(108,"Hs","Hassium",7,8,"Kim loại chuyển tiếp","[Rn] 5f14 6d6 7s2"),
(109,"Mt","Meitnerium",7,9,"Kim loại chuyển tiếp","[Rn] 5f14 6d7 7s2"),
(110,"Ds","Darmstadtium",7,10,"Kim loại chuyển tiếp","[Rn] 5f14 6d9 7s1"),
(111,"Rg","Roentgenium",7,11,"Kim loại chuyển tiếp","[Rn] 5f14 6d10 7s1"),
(112,"Cn","Copernicium",7,12,"Kim loại chuyển tiếp","[Rn] 5f14 6d10 7s2"),
(113,"Nh","Nihonium",7,13,"Kim loại","[Rn] 5f14 6d10 7s2 7p1"),
(114,"Fl","Flerovium",7,14,"Kim loại","[Rn] 5f14 6d10 7s2 7p2"),
(115,"Mc","Moscovium",7,15,"Kim loại","[Rn] 5f14 6d10 7s2 7p3"),
(116,"Lv","Livermorium",7,16,"Kim loại","[Rn] 5f14 6d10 7s2 7p4"),
(117,"Ts","Tennessine",7,17,"Halogen","[Rn] 5f14 6d10 7s2 7p5"),
(118,"Og","Oganesson",7,18,"Khí hiếm","[Rn] 5f14 6d10 7s2 7p6"),
]

ELEMENTS = [dict(Z=z,symbol=s,name=n,period=p,group=g,category=c,config=ec)
            for z,s,n,p,g,c,ec in ELEMENTS]
BY_Z = {e["Z"]: e for e in ELEMENTS}

# ============================================================
# QUY TẮC SỐ LƯỢNG TỬ
# ============================================================
# Thứ tự m_l dùng trong quy ước điền electron:
# -l, ..., 0, ..., +l; trước hết ms=+1/2 rồi ms=-1/2
# Đây là quy ước chuẩn thường dùng trong bài tập phổ thông.
SUBSHELL_ORDER = [
    (1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),
    (4,1),(5,0),(4,2),(5,1),(6,0),(4,3),(5,2),
    (6,1),(7,0),(5,3),(6,2),(7,1)
]

def capacity(l):
    return 2*(2*l+1)

def quantum_valid(n,l,ml,ms):
    if n < 1:
        return False, "n phải là số nguyên dương."
    if l < 0 or l >= n:
        return False, "Phải có 0 ≤ l < n."
    if ml < -l or ml > l:
        return False, f"mₗ phải nằm trong khoảng từ {-l} đến {l}."
    if ms not in (-0.5, 0.5):
        return False, "mₛ chỉ có thể là +1/2 hoặc −1/2."
    return True, ""

def subshell_label(n,l):
    return {0:"s",1:"p",2:"d",3:"f"}.get(l, "?")

def find_element_by_quantum(n,l,ml,ms):
    ok, msg = quantum_valid(n,l,ml,ms)
    if not ok:
        return None, msg

    # Xác định vị trí electron trong phân lớp theo Hund.
    # Ví dụ p: ml=-1,0,+1 với ms=+1/2 là electron 1,2,3;
    # sau đó mới ghép đôi với ms=-1/2.
    mls = list(range(-l,l+1))
    if ms == 0.5:
        position = mls.index(ml) + 1
    else:
        position = (2*l+1) + mls.index(ml) + 1

    # Tìm các nguyên tố có electron cuối thuộc đúng phân lớp.
    # Với các cấu hình ngoại lệ, dùng dữ liệu cấu hình thực tế bên dưới.
    target = f"{n}{subshell_label(n,l)}"
    candidates = []

    for e in ELEMENTS:
        tokens = e["config"].split()
        # bỏ khí hiếm lõi: chỉ dùng khi target nằm sau lõi
        for token in tokens:
            if token.startswith("["):
                continue
            digits = ""
            for ch in token:
                if ch.isdigit():
                    digits += ch
                else:
                    break
            orbital = token[:len(digits)]
            if orbital == target:
                exp = int(token[len(digits):])
                if exp >= position:
                    candidates.append((e, exp))

    # Nếu có ứng viên, chọn nguyên tố có đúng electron thứ position
    # trong phân lớp. Với phần lớn bài phổ thông, đó là nguyên tố mong muốn.
    if candidates:
        # ưu tiên nguyên tố mà target là phân lớp phân biệt cuối cùng
        exact = []
        for e, exp in candidates:
            # lấy token target cuối cùng trong cấu hình
            toks = [t for t in e["config"].split() if not t.startswith("[")]
            target_toks = [t for t in toks if t.startswith(target)]
            if target_toks:
                exact.append((e, int(target_toks[-1][len(target):])))
        if exact:
            exact.sort(key=lambda x: x[1])
            # Chọn nguyên tố tại đúng mức electron position.
            for e, exp in exact:
                if exp == position:
                    return e, f"Electron cuối được xác định là {target}^{position} theo quy ước điền orbital."

    # Cách chắc chắn hơn cho cấu hình Aufbau lý tưởng:
    # cộng các electron của các phân lớp trước target.
    total_before = 0
    found = False
    for nn,ll in SUBSHELL_ORDER:
        if (nn,ll) == (n,l):
            found = True
            break
        total_before += capacity(ll)
    if found:
        z = total_before + position
        if z <= 118:
            return BY_Z.get(z), f"Theo quy ước Aufbau/Hund: Z = {total_before} + {position} = {z}."

    return None, "Bộ số lượng tử hợp lệ nhưng không khớp một nguyên tố trong bộ dữ liệu hiện tại."

def shell_config(config):
    # Chuyển cấu hình thành dạng dễ đọc
    return config.replace(" ", "  ")

def characteristic(e):
    cat = e["category"]
    if cat == "Kim loại kiềm":
        return "Kim loại hoạt động mạnh, thường có 1 electron hóa trị, dễ nhường 1e."
    if cat == "Kim loại kiềm thổ":
        return "Kim loại hoạt động, thường có 2 electron hóa trị, dễ tạo ion M²⁺."
    if cat == "Halogen":
        return "Phi kim hoạt động mạnh, có 7 electron hóa trị, dễ nhận 1e."
    if cat == "Khí hiếm":
        return "Lớp electron ngoài cùng bão hòa, rất ít phản ứng ở điều kiện thường."
    if cat == "Lantanide":
        return "Kim loại đất hiếm, thường có trạng thái oxi hóa +3."
    if cat == "Actinide":
        return "Kim loại phóng xạ thuộc dãy actinide."
    if cat == "Kim loại chuyển tiếp":
        return "Có phân lớp d đang được điền hoặc chưa bão hòa; thường có nhiều số oxi hóa."
    if cat == "Á kim":
        return "Có tính chất trung gian giữa kim loại và phi kim."
    if cat == "Phi kim":
        return "Thường có xu hướng nhận hoặc dùng chung electron để đạt cấu hình bền."
    return "Kim loại; có tính dẫn điện và dẫn nhiệt đặc trưng của kim loại."

# ============================================================
# GIAO DIỆN
# ============================================================
st.title("⚛️ Quantum → Nguyên tố hóa học")
st.caption("Tra cứu nguyên tố từ 4 số lượng tử và tra cứu ngược từ số hiệu nguyên tử — không dùng AI, không cần API.")

tab1, tab2 = st.tabs(["🔬 Tìm nguyên tố bằng số lượng tử", "🧪 Tra cứu nguyên tố / Bảng tuần hoàn"])

with tab1:
    st.subheader("Nhập 4 số lượng tử của electron cuối cùng")

    c1,c2,c3,c4 = st.columns(4)
    with c1:
        n = st.number_input("Số lượng tử chính n", min_value=1, max_value=7, value=3, step=1)
    with c2:
        l = st.number_input("Số lượng tử phụ l", min_value=0, max_value=6, value=1, step=1)
    with c3:
        ml = st.number_input("Số lượng tử từ mₗ", min_value=-6, max_value=6, value=0, step=1)
    with c4:
        ms_text = st.selectbox("Số lượng tử spin mₛ", ["+1/2", "-1/2"])

    ms = 0.5 if ms_text == "+1/2" else -0.5

    if st.button("🔎 Xác định nguyên tố", type="primary", use_container_width=True):
        e, message = find_element_by_quantum(int(n), int(l), int(ml), ms)

        if e:
            st.success(f"Đã xác định: **{e['name']} ({e['symbol']}) — Z = {e['Z']}**")
            a,b,c,d = st.columns(4)
            a.metric("Số hiệu nguyên tử", e["Z"])
            b.metric("Chu kỳ", e["period"])
            c.metric("Nhóm", e["group"])
            d.metric("Phân loại", e["category"])

            st.markdown(f"""
            ### 📌 Kết quả
            - **Nguyên tố:** {e['name']} ({e['symbol']})
            - **Z:** {e['Z']}
            - **Chu kỳ:** {e['period']}
            - **Nhóm:** {e['group']}
            - **Loại:** {e['category']}
            - **Cấu hình electron:** `{e['config']}`
            - **Tính chất đặc trưng:** {characteristic(e)}
            """)

            st.info("💡 " + message)
        else:
            st.error(message)

    with st.expander("📚 Quy tắc cần nhớ"):
        st.markdown("""
        **1. Số lượng tử chính:** `n = 1, 2, 3, ...`

        **2. Số lượng tử phụ:** `0 ≤ l < n`
        - `l = 0 → s`
        - `l = 1 → p`
        - `l = 2 → d`
        - `l = 3 → f`

        **3. Số lượng tử từ:** `−l ≤ mₗ ≤ +l`

        **4. Số lượng tử spin:** `mₛ = +1/2 hoặc −1/2`

        Khi xác định electron cuối cùng, chương trình dùng quy ước:
        **điền các orbital có mₗ từ âm → dương, electron spin +1/2 trước, sau đó ghép đôi spin −1/2.**
        """)

with tab2:
    st.subheader("🔎 Tra cứu theo số hiệu nguyên tử")

    z = st.number_input("Nhập số hiệu nguyên tử Z", min_value=1, max_value=118, value=1, step=1)

    if st.button("Tra cứu nguyên tố", use_container_width=True):
        e = BY_Z[int(z)]
        st.success(f"**{e['name']} ({e['symbol']})** — Z = {e['Z']}")

        a,b,c,d,e5 = st.columns(5)
        a.metric("Z", e["Z"])
        b.metric("Ký hiệu", e["symbol"])
        c.metric("Chu kỳ", e["period"])
        d.metric("Nhóm", e["group"])
        e5.metric("Phân loại", e["category"])

        st.markdown(f"""
        ### {e['symbol']} — {e['name']}
        - **Số hiệu nguyên tử:** {e['Z']}
        - **Chu kỳ:** {e['period']}
        - **Nhóm:** {e['group']}
        - **Phân loại:** {e['category']}
        - **Cấu hình electron:** `{e['config']}`
        - **Tính chất đặc trưng:** {characteristic(e)}
        """)

    st.divider()
    st.subheader("🧩 Bảng tuần hoàn")

    # Bảng 18 cột, 7 chu kỳ
    grid = [["" for _ in range(18)] for _ in range(7)]
    for e in ELEMENTS:
        if isinstance(e["group"], int) and 1 <= e["group"] <= 18:
            grid[e["period"]-1][e["group"]-1] = f"{e['symbol']}<br><small>{e['Z']}</small>"

    # Lanthanide/actinide hiển thị riêng
    for r in range(7):
        cols = st.columns(18)
        for g in range(18):
            cell = grid[r][g]
            if cell:
                znum = next(
                    x["Z"] for x in ELEMENTS
                    if x["period"] == r+1 and x["group"] == g+1
                )
                if cols[g].button(cell.replace("<br>"," ").replace("<small>","").replace("</small>",""), key=f"cell_{znum}"):
                    st.session_state["selected_z"] = znum
            else:
                cols[g].markdown(" ")

    st.caption("Bảng trên hiển thị các nguyên tố có nhóm IUPAC 1–18. Lantanide và actinide được tra cứu bằng Z bên dưới.")

    st.markdown("### 🌟 Lantanide và Actinide")
    special = [x for x in ELEMENTS if x["category"] in ("Lantanide","Actinide")]
    cols = st.columns(15)
    for i,e in enumerate(special):
        if cols[i % 15].button(f"{e['symbol']} ({e['Z']})", key=f"special_{e['Z']}"):
            st.session_state["selected_z"] = e["Z"]

    if "selected_z" in st.session_state:
        e = BY_Z[st.session_state["selected_z"]]
        st.divider()
        st.markdown(f"## 📖 {e['name']} ({e['symbol']})")
        st.write(f"**Z = {e['Z']} · Chu kỳ {e['period']} · Nhóm {e['group']} · {e['category']}**")
        st.write(f"**Cấu hình electron:** `{e['config']}`")
        st.write(f"**Tính chất đặc trưng:** {characteristic(e)}")

st.divider()
st.caption("© Quantum → Nguyên tố | Dữ liệu 118 nguyên tố | Hoạt động offline sau khi cài Streamlit.")
