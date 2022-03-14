from typing import Any, List

def sum(data: List) -> float:
    """
    Fungsi untuk mencari jumlah seluruh daftar dari data
    
    >>> sum([3, 4, 5, 3, 2, 5, 7, 10])
    39.0
    """
    if isinstance(data, List):
        x = 0
        for i in data:
            x = x + i
        return float(x)
    else:
        raise TypeError("Hanya menerima tipe data List")


def mean(data: List) -> float:
    """
    Fungsi untuk mencari nilai rata-rata.
    mean = sum + banyak data.
    
    >>> mean([3, 4, 5, 3, 2, 5, 7, 10])
    4.875
    
    """
    if isinstance(data, List):
        s = sum(data)
        n = len(data)
        return float(s / n)
    else:
        raise TypeError("Hanya menerima tipe data list")
    
def variant(data: List) -> float:
    """
    variant = (jumlah setiap suku - rata-rata) ^ 2 / n
    
    >>> variant([8, 7, 10, 12, 9, 4, 6])
    6.0
    """
    if isinstance(data, List):
        n = len(data) # Jumlah suku
        m = mean(data) # Jumlah rata-rata
        
        v = [] # Data kosong
        for i in data:
            v.append(i - m)
        for i in range(len(v)):
            v[i] = v[i]**2
        s = sum(v) # Jumlah suku dijumlahkan dengan setiap suku
        return float(s / n)
    else:
        raise TypeError("Hanya menerima tipe data list")

def median(data: List) -> Any:
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i - 1] + data[i]) / 2
        

print(median([3, 4, 5, 6, 7]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()