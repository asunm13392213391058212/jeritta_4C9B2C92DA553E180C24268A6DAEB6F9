def ls(pl,tg):
  indices = []

  for index,product in enumerate(pl):
    if product == tg:
      indices.append(index)
  return indices

products = ["Shoes","Boot","Loafer","Shoes","Sandal","Shoes"]
target ="Shoes"
result = ls(products,target)
print(result)