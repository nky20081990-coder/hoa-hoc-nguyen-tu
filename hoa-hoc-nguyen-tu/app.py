import streamlit as st

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="Phòng thí nghiệm số lượng tử",
    page_icon="⚛️",
    layout="wide"
)

# =========================================================
# 118 NGUYÊN TỐ
# =========================================================

ELEMENT_DATA = [
    (1, "H", "Hydrogen", 1, 1, "Phi kim"),
    (2, "He", "Helium", 1, 18, "Khí hiếm"),

    (3, "Li", "Lithium", 2, 1, "Kim loại kiềm"),
    (4, "Be", "Beryllium", 2, 2, "Kim loại kiềm thổ"),
    (5, "B", "Boron", 2, 13, "Á kim"),
    (6, "C", "Carbon", 2, 14, "Phi kim"),
    (7, "N", "Nitrogen", 2, 15, "Phi kim"),
    (8, "O", "Oxygen", 2, 16, "Phi kim"),
    (9, "F", "Fluorine", 2, 17, "Halogen"),
    (10, "Ne", "Neon", 2, 18, "Khí hiếm"),

    (11, "Na", "Sodium", 3, 1, "Kim loại kiềm"),
    (12, "Mg", "Magnesium", 3, 2, "Kim loại kiềm thổ"),
    (13, "Al", "Aluminium", 3, 13, "Kim loại"),
    (14, "Si", "Silicon", 3, 14, "Á kim"),
    (15, "P", "Phosphorus", 3, 15, "Phi kim"),
    (16, "S", "Sulfur", 3, 16, "Phi kim"),
    (17, "Cl", "Chlorine", 3, 17, "Halogen"),
    (18, "Ar", "Argon", 3, 18, "Khí hiếm"),

    (19, "K", "Potassium", 4, 1, "Kim loại kiềm"),
    (20, "Ca", "Calcium", 4, 2, "Kim loại kiềm thổ"),
    (21, "Sc", "Scandium", 4, 3, "Kim loại chuyển tiếp"),
    (22, "Ti", "Titanium", 4, 4, "Kim loại chuyển tiếp"),
    (23, "V", "Vanadium", 4, 5, "Kim loại chuyển tiếp"),
    (24, "Cr", "Chromium", 4, 6, "Kim loại chuyển tiếp"),
    (25, "Mn", "Manganese", 4, 7, "Kim loại chuyển tiếp"),
    (26, "Fe", "Iron", 4, 8, "Kim loại chuyển tiếp"),
    (27, "Co", "Cobalt", 4, 9, "Kim loại chuyển tiếp"),
    (28, "Ni", "Nickel", 4, 10, "Kim loại chuyển tiếp"),
    (29, "Cu", "Copper", 4, 11, "Kim loại chuyển tiếp"),
    (30, "Zn", "Zinc", 4, 12, "Kim loại chuyển tiếp"),
    (31, "Ga", "Gallium", 4, 13, "Kim loại"),
    (32, "Ge", "Germanium", 4, 14, "Á kim"),
    (33, "As", "Arsenic", 4, 15, "Á kim"),
    (34, "Se", "Selenium", 4, 16, "Phi kim"),
    (35, "Br", "Bromine", 4, 17, "Halogen"),
    (36, "Kr", "Krypton", 4, 18, "Khí hiếm"),

    (37, "Rb", "Rubidium", 5, 1, "Kim loại kiềm"),
    (38, "Sr", "Strontium", 5, 2, "Kim loại kiềm thổ"),
    (39, "Y", "Yttrium", 5, 3, "Kim loại chuyển tiếp"),
    (40, "Zr", "Zirconium", 5, 4, "Kim loại chuyển tiếp"),
    (41, "Nb", "Niobium", 5, 5, "Kim loại chuyển tiếp"),
    (42, "Mo", "Molybdenum", 5, 6, "Kim loại chuyển tiếp"),
    (43, "Tc", "Technetium", 5, 7, "Kim loại chuyển tiếp"),
    (44, "Ru", "Ruthenium", 5, 8, "Kim loại chuyển tiếp"),
    (45, "Rh", "Rhodium", 5, 9, "Kim loại chuyển tiếp"),
    (46, "Pd", "Palladium", 5, 10, "Kim loại chuyển tiếp"),
    (47, "Ag", "Silver", 5, 11, "Kim loại chuyển tiếp"),
    (48, "Cd", "Cadmium", 5, 12, "Kim loại chuyển tiếp"),
    (49, "In", "Indium", 5, 13, "Kim loại"),
    (50, "Sn", "Tin", 5, 14, "Kim loại"),
    (51, "Sb", "Antimony", 5, 15, "Á kim"),
    (52, "Te", "Tellurium", 5, 16, "Á kim"),
    (53, "I", "Iodine", 5, 17, "Halogen"),
    (54, "Xe", "Xenon", 5, 18, "Khí hiếm"),

    (55, "Cs", "Cesium", 6, 1, "Kim loại kiềm"),
    (56, "Ba", "Barium", 6, 2, "Kim loại kiềm thổ"),

    (57, "La", "Lanthanum", 6, 3, "Lantanide"),
    (58, "Ce", "Cerium", 6, 3, "Lantanide"),
    (59, "Pr", "Praseodymium", 6, 3, "Lantanide"),
    (60, "Nd", "Neodymium", 6, 3, "Lantanide"),
    (61, "Pm", "Promethium", 6, 3, "Lantanide"),
    (62, "Sm", "Samarium", 6, 3, "Lantanide"),
    (63, "Eu", "Europium", 6, 3, "Lantanide"),
    (64, "Gd", "Gadolinium", 6, 3, "Lantanide"),
    (65, "Tb", "Terbium", 6, 3, "Lantanide"),
    (66, "Dy", "Dysprosium", 6, 3, "Lantanide"),
    (67, "Ho", "Holmium", 6, 3, "Lantanide"),
    (68, "Er", "Erbium", 6, 3, "Lantanide"),
    (69, "Tm", "Thulium", 6, 3, "Lantanide"),
    (70, "Yb", "Ytterbium", 6, 3, "Lantanide"),
    (71, "Lu", "Lutetium", 6, 3, "Lantanide"),

    (72, "Hf", "Hafnium", 6, 4, "Kim loại chuyển tiếp"),
    (73, "Ta", "Tantalum", 6, 5, "Kim loại chuyển tiếp"),
    (74, "W", "Tungsten", 6, 6, "Kim loại chuyển tiếp"),
    (75, "Re", "Rhenium", 6, 7, "Kim loại chuyển tiếp"),
    (76, "Os", "Osmium", 6, 8, "Kim loại chuyển tiếp"),
    (77, "Ir", "Iridium", 6, 9, "Kim loại chuyển tiếp"),
    (78, "Pt", "Platinum", 6, 10, "Kim loại chuyển tiếp"),
    (79, "Au", "Gold", 6, 11, "Kim loại chuyển tiếp"),
    (80, "Hg", "Mercury", 6, 12, "Kim loại chuyển tiếp"),
    (81, "Tl", "Thallium", 6, 13, "Kim loại"),
    (82, "Pb", "Lead", 6, 14, "Kim loại"),
    (83, "Bi", "Bismuth", 6, 15, "Kim loại"),
    (84, "Po", "Polonium", 6, 16, "Á kim"),
    (85, "At", "Astatine", 6, 17, "Halogen"),
    (86, "Rn", "Radon", 6, 18, "Khí hiếm"),

    (87, "Fr", "Francium", 7, 1, "Kim loại kiềm"),
    (88, "Ra", "Radium", 7, 2, "Kim loại kiềm thổ"),

    (89, "Ac", "Actinium", 7, 3, "Actinide"),
    (90, "Th", "Thorium", 7, 3, "Actinide"),
    (91, "Pa", "Protactinium", 7, 3, "Actinide"),
    (92, "U", "Uranium", 7, 3, "Actinide"),
    (93, "Np", "Neptunium", 7, 3, "Actinide"),
    (94, "Pu", "Plutonium", 7, 3, "Actinide"),
    (95, "Am", "Americium", 7, 3, "Actinide"),
    (96, "Cm", "Curium", 7, 3, "Actinide"),
    (97, "Bk", "Berkelium", 7, 3, "Actinide"),
    (98, "Cf", "Californium", 7, 3, "Actinide"),
    (99, "Es", "Einsteinium", 7, 3, "Actinide"),
    (100, "Fm", "Fermium", 7, 3, "Actinide"),
    (101, "Md", "Mendelevium", 7, 3, "Actinide"),
    (102, "No", "Nobelium", 7, 3, "Actinide"),
    (103, "Lr", "Lawrencium", 7, 3, "Actinide"),

    (104, "Rf", "Rutherfordium", 7, 4, "Kim loại chuyển tiếp"),
    (105, "Db", "Dubnium", 7, 5, "Kim loại chuyển tiếp"),
    (106, "Sg", "Seaborgium", 7, 6, "Kim loại chuyển tiếp"),
    (107, "Bh", "Bohrium", 7, 7, "Kim loại chuyển tiếp"),
    (108, "Hs", "Hassium", 7, 8, "Kim loại chuyển tiếp"),
    (109, "Mt", "Meitnerium", 7, 9, "Kim loại chuyển tiếp"),
    (110, "Ds", "Darmstadtium", 7, 10, "Kim loại chuyển tiếp"),
    (111, "Rg", "Roentgenium", 7, 11, "Kim loại chuyển tiếp"),
    (112, "Cn", "Copernicium", 7, 12, "Kim loại chuyển tiếp"),
    (113, "Nh", "Nihonium", 7, 13, "Kim loại"),
    (114, "Fl", "Flerovium", 7, 14, "Kim loại"),
    (115, "Mc", "Moscovium", 7, 15, "Kim loại"),
    (116, "Lv", "Livermorium", 7, 16, "Kim loại"),
    (117, "Ts", "Tennessine", 7, 17, "Halogen"),
    (118, "Og", "Oganesson", 7, 18, "Khí hiếm"),
]

ELEMENTS = {
    z: {
        "symbol": symbol,
        "name": name,
        "period": period,
        "group": group,
        "type": kind
    }
    for z, symbol, name, period, group, kind in ELEMENT_DATA
}

# =========================================================
# THỨ TỰ AUFBAU
# =========================================================

AUFBAU = [
    (1, 0, "1s", 2),
    (2, 0, "2s", 2),
    (2, 1, "2p", 6),
    (3, 0, "3s", 2),
    (3, 1, "3p", 6),
    (4, 0, "4s", 2),
    (3, 2, "3d", 10),
    (4, 1, "4p", 6),
    (5, 0, "5s", 2),
    (4, 2, "4d", 10),
    (5, 1, "5p", 6),
    (6, 0, "6s", 2),
    (4, 3, "4f", 14),
    (5, 2, "5d", 10),
    (6, 1, "6p", 6),
    (7, 0, "7s", 2),
    (5, 3, "5f", 14),
    (6, 2, "6d", 10),
    (7, 1, "7p", 6),
]

# =========================================================
# CẤU HÌNH NGOẠI LỆ QUAN TRỌNG
# =========================================================

EXCEPTIONS = {
    24: "1s2 2s2 2p6 3s2 3p6 3d5 4s1",
    29: "1s2 2s2 2p6 3s2 3p6 3d10 4s1",

    41: "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d4 5s1",
    42: "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s1",
    44: "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d7 5s1",
    45: "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d8 5s1",
    46: "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10",
    47: "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s1",

    78: "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d9 6s1",
    79: "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s1",

    103: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 7p1",
}

# =========================================================
# PARSE CẤU HÌNH ELECTRON
# =========================================================

def parse_config(config):
    result = []

    for part in config.split():
        orbital = part[:-1]
        electrons = int(part[-1])

        n = int(orbital[0])
        letter = orbital[1]

        l_map = {
            "s": 0,
            "p": 1,
            "d": 2,
            "f": 3
        }

        l = l_map[letter]

        result.append({
            "orbital": orbital,
            "n": n,
            "l": l,
            "electrons": electrons
        })

    return result


# =========================================================
# CẤU HÌNH ELECTRON THEO AUFBAU
# =========================================================

def aufbau_config(z):

    remaining = z
    result = []

    for n, l, orbital, capacity in AUFBAU:

        if remaining <= 0:
            break

        e = min(remaining, capacity)

        result.append({
            "orbital": orbital,
            "n": n,
            "l": l,
            "electrons": e
        })

        remaining -= e

    return result


def electron_config(z):

    if z in EXCEPTIONS:
        return parse_config(EXCEPTIONS[z])

    return aufbau_config(z)


# =========================================================
# TÌM PHÂN LỚP CUỐI CÙNG
# =========================================================

def differentiating_subshell(z):

    config = electron_config(z)

    if not config:
        return None

    # Nguyên tố khí hiếm:
    # lấy phân lớp cuối cùng trong cấu hình
    return config[-1]


# =========================================================
# XÁC ĐỊNH SỐ LƯỢNG TỬ CỦA ELECTRON CUỐI
# =========================================================

def electron_quantum_numbers(subshell, electron_number):

    l = subshell["l"]

    orbitals = list(range(-l, l + 1))

    # Quy ước:
    # điền electron độc thân trước
    # m_s = +1/2
    #
    # sau đó ghép đôi
    # m_s = -1/2

    number_orbitals = len(orbitals)

    if electron_number <= number_orbitals:

        index = electron_number - 1

        ml = orbitals[index]
        ms = "+1/2"

    else:

        index = electron_number - number_orbitals - 1

        ml = orbitals[index]
        ms = "-1/2"

    return {
        "n": subshell["n"],
        "l": l,
        "ml": ml,
        "ms": ms
    }


# =========================================================
# TÍNH ELECTRON CUỐI CÙNG
# =========================================================

def last_electron_quantum_numbers(z):

    config = electron_config(z)

    last = config[-1]

    return electron_quantum_numbers(
        last,
        last["electrons"]
    )


# =========================================================
# VALIDATE SỐ LƯỢNG TỬ
# =========================================================

def validate_quantum_numbers(n, l, ml, ms):

    errors = []

    if n < 1:
        errors.append(
            "n phải là số nguyên dương."
        )

    if l < 0 or l >= n:
        errors.append(
            f"Với n = {n}, phải có 0 ≤ l ≤ {n - 1}."
        )

    if ml < -l or ml > l:
        errors.append(
            f"Với l = {l}, phải có -{l} ≤ mₗ ≤ {l}."
        )

    if ms not in ["+1/2", "-1/2"]:
        errors.append(
            "mₛ chỉ nhận +1/2 hoặc -1/2."
        )

    return errors


# =========================================================
# TÌM NGUYÊN TỐ TỪ 4 SỐ LƯỢNG TỬ
# =========================================================

def search_by_quantum_numbers(n, l, ml, ms):

    matches = []

    for z in ELEMENTS:

        q = last_electron_quantum_numbers(z)

        if (
            q["n"] == n
            and q["l"] == l
            and q["ml"] == ml
            and q["ms"] == ms
        ):
            matches.append(z)

    return matches


# =========================================================
# HIỂN THỊ CẤU HÌNH
# =========================================================

def config_to_string(z):

    config = electron_config(z)

    return " ".join(
        f"{x['orbital']}{x['electrons']}"
        for x in config
    )


# =========================================================
# THÔNG TIN NGUYÊN TỐ
# =========================================================

def show_element(z):

    element = ELEMENTS[z]

    st.markdown(
        f"# ⚛️ {element['name']} ({element['symbol']})"
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.metric(
            "Số hiệu nguyên tử",
            z
        )

    with c2:
        st.metric(
            "Ký hiệu",
            element["symbol"]
        )

    with c3:
        st.metric(
            "Chu kỳ",
            element["period"]
        )

    with c4:
        st.metric(
            "Nhóm",
            element["group"]
        )

    with c5:
        st.metric(
            "Phân loại",
            element["type"]
        )

    st.markdown("---")

    st.markdown("### ⚡ Cấu hình electron")

    st.code(
        config_to_string(z),
        language="text"
    )

    st.markdown(
        "### 🔢 Bộ số lượng tử của electron cuối"
    )

    q = last_electron_quantum_numbers(z)

    st.info(
        f"n = {q['n']} | "
        f"l = {q['l']} | "
        f"mₗ = {q['ml']} | "
        f"mₛ = {q['ms']}"
    )

    st.markdown("### 📚 Đặc trưng")

    descriptions = {
        "Kim loại kiềm":
            "Có 1 electron hóa trị, dễ nhường electron và thường tạo ion +1.",

        "Kim loại kiềm thổ":
            "Có 2 electron hóa trị, thường tạo ion +2.",

        "Kim loại chuyển tiếp":
            "Có các phân lớp d liên quan đến tính chất hóa học và nhiều số oxi hóa.",

        "Kim loại":
            "Có tính dẫn điện, dẫn nhiệt và thường có xu hướng nhường electron.",

        "Phi kim":
            "Thường có xu hướng nhận electron hoặc dùng chung electron.",

        "Halogen":
            "Có 7 electron lớp ngoài cùng và thường tạo ion -1.",

        "Khí hiếm":
            "Có lớp electron hóa trị tương đối bền vững.",

        "Á kim":
            "Có tính chất trung gian giữa kim loại và phi kim.",

        "Lantanide":
            "Các nguyên tố đất hiếm, liên quan đến sự điền electron vào phân lớp 4f.",

        "Actinide":
            "Các nguyên tố có tính phóng xạ, liên quan đến sự điền electron vào phân lớp 5f."
    }

    st.write(
        descriptions.get(
            element["type"],
            "Đang cập nhật."
        )
    )


# =========================================================
# TRANG TÌM BẰNG SỐ LƯỢNG TỬ
# =========================================================

def quantum_page():

    st.title(
        "⚛️ TÌM NGUYÊN TỐ BẰNG 4 SỐ LƯỢNG TỬ"
    )

    st.write(
        "Nhập bộ số lượng tử của electron cuối cùng."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        n = st.number_input(
            "n – số lượng tử chính",
            1,
            7,
            3
        )

    with c2:
        l = st.number_input(
            "l – số lượng tử phụ",
            0,
            3,
            2
        )

    with c3:
        ml = st.number_input(
            "mₗ – số lượng tử từ",
            -3,
            3,
            2
        )

    with c4:
        ms = st.selectbox(
            "mₛ – số lượng tử spin",
            ["+1/2", "-1/2"]
        )

    if st.button(
        "🔎 XÁC ĐỊNH NGUYÊN TỐ",
        type="primary",
        use_container_width=True
    ):

        errors = validate_quantum_numbers(
            n,
            l,
            ml,
            ms
        )

        if errors:

            st.error(
                "Bộ số lượng tử không hợp lệ."
            )

            for error in errors:
                st.warning(error)

            return

        matches = search_by_quantum_numbers(
            n,
            l,
            ml,
            ms
        )

        st.markdown("---")

        if not matches:

            st.warning(
                "Không tìm thấy nguyên tố nào có đúng bộ số lượng tử "
                "này theo quy ước electron cuối được sử dụng trong hệ thống."
            )

            st.info(
                "Hãy kiểm tra lại xem bạn đang nhập số lượng tử của "
                "electron cuối cùng hay của một electron bất kỳ."
            )

            return

        if len(matches) > 1:

            st.warning(
                "Bộ số lượng tử này trùng với quy ước electron cuối "
                "của nhiều nguyên tố. Hệ thống liệt kê các khả năng:"
            )

        for z in matches:

            element = ELEMENTS[z]

            st.success(
                f"🎯 {element['name']} ({element['symbol']}) — Z = {z}"
            )

        # Nếu duy nhất
        if len(matches) == 1:

            z = matches[0]

            element = ELEMENTS[z]

            st.markdown("## 🧠 GIẢI THÍCH TỪNG BƯỚC")

            st.write(
                f"**Bước 1:** n = {n} → electron thuộc lớp thứ {n}."
            )

            l_name = {
                0: "s",
                1: "p",
                2: "d",
                3: "f"
            }[l]

            st.write(
                f"**Bước 2:** l = {l} → electron thuộc phân lớp {l_name}."
            )

            st.write(
                f"**Bước 3:** mₗ = {ml} → xác định một orbital "
                f"trong phân lớp {l_name}."
            )

            st.write(
                f"**Bước 4:** mₛ = {ms} → xác định chiều spin của electron."
            )

            st.write(
                f"**Bước 5:** Tra cấu hình electron trạng thái cơ bản "
                f"→ xác định electron cuối."
            )

            st.markdown(
                f"""
                ## 🎯 KẾT LUẬN

                **n = {n} ; l = {l} ; mₗ = {ml} ; mₛ = {ms}**

                ⬇️

                **Nguyên tố: {element['name']} ({element['symbol']})**

                **Số hiệu nguyên tử: Z = {z}**

                **Chu kỳ: {element['period']}**

                **Nhóm: {element['group']}**
                """
            )

            st.markdown("### ⚡ Cấu hình electron")

            st.code(
                config_to_string(z)
            )


# =========================================================
# BẢNG TUẦN HOÀN
# =========================================================

def periodic_table():

    st.title("🧪 BẢNG TUẦN HOÀN TƯƠNG TÁC")

    # Hiển thị 18 nhóm
    for period in range(1, 8):

        cols = st.columns(18)

        for group in range(1, 19):

            found = None

            for z, element in ELEMENTS.items():

                if (
                    element["period"] == period
                    and element["group"] == group
                    and not (
                        57 <= z <= 71
                        or 89 <= z <= 103
                    )
                ):
                    found = z
                    break

            if found:

                element = ELEMENTS[found]

                if cols[group - 1].button(
                    f"{element['symbol']}\n{found}",
                    key=f"p_{period}_{group}"
                ):

                    st.session_state["selected_z"] = found

            else:

                cols[group - 1].write("")

    st.markdown("---")

    st.write("**Lantanide**")

    cols = st.columns(15)

    for i, z in enumerate(range(57, 72)):

        element = ELEMENTS[z]

        if cols[i].button(
            f"{element['symbol']}\n{z}",
            key=f"lan_{z}"
        ):

            st.session_state["selected_z"] = z

    st.write("**Actinide**")

    cols = st.columns(15)

    for i, z in enumerate(range(89, 104)):

        element = ELEMENTS[z]

        if cols[i].button(
            f"{element['symbol']}\n{z}",
            key=f"act_{z}"
        ):

            st.session_state["selected_z"] = z


# =========================================================
# TRA CỨU
# =========================================================

def lookup_page():

    st.title(
     
