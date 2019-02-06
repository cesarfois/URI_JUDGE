import math

a, b = map(float,input().split())
c, d = map(float,input().split())


print('A = %.6f, B = %.6f' % (a, b))
print('C = {:.6f}, D = {:.6f}'.format(c, d))

print('A = {:.1f}, B = {:.1f}'.format(a, b))
print('C = {:.1f}, D = {:.1f}'.format(c, d))

print('A = {:.2f}, B = {:.2f}'.format(a, b))
print('C = {:.2f}, D = {:.2f}'.format(c, d))

print('A = {:.3f}, B = {:.3f}'.format(a, b))
print('C = {:.3f}, D = {:.3f}'.format(c, d))


print('A = {:.3E}, B = {:.3E}'.format(a, b))
print('C = {:.3E}, D = {:.3E}'.format(c, d))

print('A = {}, B = {}'.format(int(math.ceil(a)), int(math.ceil(b))))
print('C = {}, D = {}'.format(int(math.ceil(c)), int(math.ceil(d))))