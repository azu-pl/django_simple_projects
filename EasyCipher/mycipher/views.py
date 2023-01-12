from django.shortcuts import render, Http404

# Create your views here.
def rotn_code(request, n, slug):
    if n < 1 or n > 20:
        raise Http404('Nie właściwy zakres przesunięcia 1-20')
    coded_msg = ""

    start = ord("a")
    end = ord("z")

    for i in slug:
        if "a" <= i <= "z":
            new_ch = ord(i) + n

            if new_ch > end:
                offset = new_ch - end
                new_ch = start + offset - 1
            i = chr(new_ch)

        coded_msg = coded_msg + i
    ctx = {'message': slug, 'coded': coded_msg, 'offset': n}

    return render(request, 'mycipher/rotn_coded.html', ctx)

def rotn_decode(request, n, slug):
    if n < 1 or n > 20:
        raise Http404('Nie właściwy zakres przesunięcia 1-20')
    coded_msg = ""

    start = ord("a")
    end = ord("z")

    for i in slug:
        if "a" <= i <= "z":
            new_ch = ord(i) - n

            if new_ch < start:
                offset = new_ch - start
                new_ch = end + offset + 1
            i = chr(new_ch)

        coded_msg = coded_msg + i
    ctx = {'message': slug, 'coded': coded_msg, 'offset': n}

    return render(request, 'mycipher/rotn_coded.html', ctx)

def adbash_coded(request, slug):
    coded_msg = ""
    start = ord("a")
    end = ord("z")
    for i in slug:
        if "a" <= i <= "z":
            offset = ord(i) - start
            new_ch = end - offset
            i = chr(new_ch)

        coded_msg += i
    ctx = {'message': slug, 'coded': coded_msg}

    return render(request, 'mycipher/adbash_coded.html', ctx)