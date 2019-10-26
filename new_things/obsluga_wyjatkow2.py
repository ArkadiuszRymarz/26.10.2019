
try:
    raise Exception("Dzwoń po policje")
except Exception:
    print("Tutaj sie jeszcze nie wywaliłem")
raise Exception("inny error")