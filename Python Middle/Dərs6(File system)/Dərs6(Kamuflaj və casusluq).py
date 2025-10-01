# əməliyyat sistemi (os) modulu/kitabxanasını iş üçün əlavə edirik
import os

def file_collector(path):
    # ünvanı (path) normallaşdırırıq
    path = os.path.normpath(path)
    result = {"dirs": [], "files": []}
    # ünvan üzrə "gəzəcək" və qovluqları, faylları axtaracaq
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
        for file in filenames:
            result["files"].append(file)
    # "skiper.txt" faylını UTF-8(Unicode) kodlamasında yazma rejimində açırıq
    # Azərbaycan dilinin əlifbasını qəbul eliyə bilsin deyə
    with open("skiper.txt", "w", encoding="utf-8") as main_file:
        main_file.write("\n{:-<50}\n".format("Qovluqlar"))
        for dir in result["dirs"]:
            main_file.write(f"\t{dir}\n")
        main_file.write("\n{:-<50}\n".format("Fayllar"))
        for file in result["files"]:
            main_file.write(f"\t{file}\n")

file_collector("C:\\Users\\rzayev_a\\MWOct_323_3_16-30_az\\Python Middle")