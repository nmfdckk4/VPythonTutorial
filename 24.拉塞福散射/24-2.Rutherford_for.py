"""
 VPython教學: 24-2.拉塞福散射, 用 for 迴圈依序代入 b = 0, 1, 2, 3, ..., 10
 Ver. 1: 2018/4/8
 Ver. 2: 2019/9/19
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 長度單位 nm, 質量單位 amu, 電量單位 e, 時間單位 ns
"""
r1, m1, q1 = 0.4, 4, 2     # 氦原子核半徑(放大後)、質量、電量
r2, m2, q2, c2 = 1, 197, 79, color.yellow  # 金原子核半徑(放大後)、質量、電量、顏色
v0 = vec(10, 0, 0)         # 氦原子核初速度
L, k = 40, 1               # 畫面長、寬, 假的靜電力常數
t, dt = 0, 0.001           # 時間, 時間間隔

"""
 2. 畫面設定
"""
# 產生動畫視窗
scene = canvas(title="Rutherford Scattering", width=800, height=600, x=0, y=0,
               center=vec(0, 0, 0), background=color.black)
# 產生金原子核
au = sphere(pos=vec(0, 0, 0), radius=r2, m=m2, q=q2, color=c2)

"""
 3. 用 for 迴圈依序代入 b = 0, 1, 2, 3, ..., n
"""
n = 10
for i in range(0, n+1, 1):
# 產生氦原子核
    alpha = sphere(pos=vec(-L/2 + r1, i, 0), radius=r1, m=m1, q=q1, v=v0,
                   color=vec((n-i)/n, 0, i/n), make_trail=True)
# 產生表示速度、加速度的箭頭
    arrow_v = arrow(pos=alpha.pos, shaftwidth=0.5*r1, color=color.cyan)
    arrow_a = arrow(pos=alpha.pos, shaftwidth=0.5*r1, color=color.magenta)
# 物體運動部分
    while(abs(alpha.pos.x) < L/2 and abs(alpha.pos.y) < L/2):
        rate(500)
# 計算氦原子核所受合力, 更新氦原子核加速度、速度、位置
        F = k*alpha.q*au.q / alpha.pos.mag2 * alpha.pos.norm()
        alpha.a = F/alpha.m
        alpha.v += alpha.a*dt
        alpha.pos += alpha.v*dt
# 更新表示速度、加速度的箭頭
        arrow_v.pos = alpha.pos
        arrow_a.pos = alpha.pos
        arrow_v.axis = alpha.v
        arrow_a.axis = alpha.a
# 更新時間
        t += dt
# 於 while 迴圈結束時隱藏箭頭
    arrow_v.visible = False
    arrow_a.visible = False
# 印出 b - y 數值
    print(i, alpha.pos.y - i)
