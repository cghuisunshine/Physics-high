from pathlib import Path
import base64
import html
import json
import subprocess
from english_content import LESSONS_EN, QUESTIONS_EN

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work'
LESSONS = {
    7: '常见力与受力分析',
    8: '力的合成分解与平衡',
    9: '动态平衡',
    10: '牛顿运动定律',
    11: '牛二律的基础应用',
}

questions = []

def q(lesson, number, page, title, text, options, answer, steps, formula, trap, crop=None, alt=''):
    questions.append(dict(id=f'l{lesson}-q{number}', lesson=lesson, number=number,
        page=page, title=title, text=text, options=options, answer=answer,
        steps=steps, formula=formula, trap=trap, crop=crop, alt=alt))

q(7,1,2,'从压缩到伸长的弹簧',
  '如图所示，两个质量均为 1 kg 的相同物块 A、B 用一个劲度系数为 500 N/m 的轻弹簧连接，两物块都处于静止状态。现用竖直力 F 缓慢地向上拉物块 A，直到物块 B 刚好离开水平地面为止。取 g = 10 m/s²，这个过程中物块 A 移动的距离是（　）。',
  ['1 cm','2 cm','4 cm','8 cm'], 'C，4 cm',[
  '初态对 A 受力分析：重力 mg 向下，弹簧支持力向上。由平衡得 kx₁ = mg，故弹簧最初被压缩 x₁ = 10/500 m = 2 cm。',
  'B 刚要离地时，地面对 B 的支持力变为零。弹簧必须向上拉 B，因此弹簧已伸长，且 kx₂ = mg，得 x₂ = 2 cm。',
  '在此之前 B 的位置不变。A 的上移距离等于弹簧从压缩 2 cm 到伸长 2 cm 的总长度变化：Δh = x₁ + x₂ = 4 cm。'],
  'Δh = mg/k + mg/k = 2mg/k = 0.04 m',
  '初态是压缩，末态是伸长，两段形变量要相加。', (590,340,150,220), '上方物块 A 与落在地面的物块 B 由竖直弹簧连接，A 受向上的拉力 F。')

q(7,2,2,'弹力大小与弹力方向',
  '如图所示为一轻质弹簧的弹力和长度的关系图像（轻质弹簧未超过弹性限度），下列说法正确的是（　）。',
  ['弹簧的原长为 6 cm','弹簧的劲度系数为 10 N/m','弹簧在长度分别为 4 cm 和 8 cm 时受到的弹力相同','在该弹簧两端各加 0.5 N 的拉力，静止时弹簧的长度为 6.5 cm'], 'A、D',[
  '图像在 ℓ = 6 cm 时弹力为零，因此弹簧原长 ℓ₀ = 6 cm，A 正确。',
  '取图上 (8 cm, 2 N)：形变量为 0.02 m，k = 2/0.02 = 100 N/m，B 错误。',
  '4 cm 和 8 cm 分别对应压缩和伸长 2 cm。弹力大小都为 2 N，但对同一端而言弹力方向相反，不能说弹力相同，C 错误。',
  '两端各加 0.5 N 的拉力，弹簧中的拉力是 0.5 N。伸长量 x = 0.5/100 m = 0.5 cm，长度应为 6.5 cm，D 正确。'],
  'F = k|ℓ − ℓ₀|；k = 100 N/m；ℓ = 6 cm + 0.5 cm = 6.5 cm',
  '弹力是矢量：大小相同不等于弹力相同。两端拉力不相加。', (530,705,270,165), 'V 形弹力大小图：长度为 6 cm 时弹力为零，4 cm 与 8 cm 时弹力均为 2 N。')

q(7,3,2,'木板抽动时的滑动摩擦',
  '如图所示，足够长的长木板 B 放在水平地面上，木块 A 放在 B 上，右侧通过一段轻绳与水平弹簧测力计的挂钩连接。现用大小为 F 的水平拉力作用在 B 上使其在水平面上向左运动。稳定时，水平弹簧测力计的示数为 Fₜ，下列说法正确的是（　）。',
  ['木块 A 受到的摩擦力为静摩擦力','无论木板 B 的速度为多大，A、B 间的摩擦力都等于 Fₜ','长木板 B 向左加速运动时，A、B 间的摩擦力变大','长木板 B 向左减速运动时，A、B 间的摩擦力减小'], 'B',[
  '木块 A 被绳固定，木板 B 向左运动，A、B 接触面有相对滑动，所以 A 受到的是向左的滑动摩擦力。',
  'A 在水平方向平衡，向右的绳拉力等于向左的滑动摩擦力，因此 f = Fₜ。',
  '按高中滑动摩擦模型，f = μN = μm_Ag。材料和压力不变，摩擦力与木板的速度及加速度无关，因此 B 正确，C、D 错误。'],
  'f = μN = μm_Ag = Fₜ',
  'B 选项适用于木板仍相对 A 滑动的过程；木板停止后应重新判断摩擦状态。', (470,1200,390,120), '木块 A 由右侧固定的测力计拉住，下面的木板 B 被向左抽动。')

q(7,4,3,'先判断静摩擦还是滑动摩擦',
  '如图所示，一质量不计的弹簧原长为 10 cm，一端固定于质量 m = 2 kg 的物体上，另一端施一水平拉力 F。已知物体与水平面间的动摩擦因数为 0.2，设最大静摩擦力与滑动摩擦力相等，取 g = 10 m/s²。\n（1）当弹簧拉长至 12 cm 时，物体恰好匀速运动，弹簧的劲度系数为多大？\n（2）若将弹簧拉长至 11 cm，物体受到的摩擦力大小为多少？\n（3）若将弹簧拉长至 13 cm，物体受到的摩擦力大小为多少？',
  [], '（1）200 N/m；（2）2 N（从静止加载）；（3）4 N',[
  '竖直方向 N = mg = 20 N。滑动摩擦力和最大静摩擦力均为 μN = 0.2 × 20 = 4 N。',
  '（1）匀速时弹簧拉力等于 4 N。弹簧伸长量为 12 − 10 = 2 cm = 0.02 m，所以 k = 4/0.02 = 200 N/m。',
  '（2）按各小问分别从静止状态加载的通常理解，长度为 11 cm 时拉力为 k × 0.01 = 2 N，小于最大静摩擦力，物体保持静止，静摩擦力为 2 N。',
  '（3）长度为 13 cm 时拉力为 k × 0.03 = 6 N，超过最大静摩擦力，物体滑动，摩擦力为 4 N。'],
  'f_max = μmg = 4 N；k = 200 N/m；F_11 = 2 N；F_13 = 6 N',
  '第（2）问有状态前提：若物体原来仍在滑动，摩擦力为 4 N，不能仅凭弹簧长度断定为 2 N。', (510,240,380,90), '水平弹簧连接地面上的物体，弹簧右端受到向右拉力。')

q(7,5,3,'磁吸块与通知纸的受力',
  '如图，某办公室有一竖直铁质的公告栏，通知纸用磁吸块压在公告栏上面，下列说法正确的是（　）。',
  ['通知纸受到 4 个力作用','磁吸块受到的摩擦力方向竖直向下','通知纸受到公告栏的摩擦力大小大于其自身重力大小','磁吸块对通知纸的压力和公告栏对通知纸的压力是一对相互作用力'], 'C',[
  '先分析磁吸块：重力向下，纸对磁吸块的静摩擦力向上，与其重力平衡。所以 B 错误。',
  '由牛顿第三定律，磁吸块对纸的摩擦力向下，大小等于磁吸块的重力。',
  '纸在竖直方向受到自身重力、磁吸块向下的摩擦力、公告栏向上的摩擦力。因此公告栏的摩擦力 f = G_纸 + G_磁吸块 > G_纸，C 正确。',
  '纸还受到两侧的两个压力，共受 5 个力，A 错误。D 中两个压力都作用在纸上，不是一对相互作用力，D 错误。'],
  'f_栏→纸 = G_纸 + G_磁吸块',
  '相互作用力必须作用在两个不同物体上。纸并不因磁吸块而直接受到磁力。', (510,535,350,155), '通知纸由磁吸块压在竖直公告栏上。')

q(8,1,2,'弓弦张力的合成',
  '射箭比赛所用的弓如图所示，已知弓的顶部跨度为 ℓ，且拉弓过程中顶部跨度保持不变；弦光滑均匀且弹性良好，其自由长度为 ℓ，劲度系数为 k。发射箭时箭连同附加装置处于弦正中间，弦的长度为 2ℓ，设弦的弹力满足胡克定律，则发射瞬间弦的弹力大小为________，此时弦对箭的作用力大小为________。',
  [], 'kℓ；√3 kℓ',[
  '整根弦由原长 ℓ 伸长到 2ℓ，伸长量为 ℓ。胡克定律给出弦内张力 T = kℓ。',
  '箭处于弦的中点，故两段弦各长 ℓ。两固定端之间的距离也为 ℓ，三条边组成等边三角形，两段弦在箭处的夹角为 60°。',
  '两段弦对箭的拉力大小均为 T，沿两段弦指向固定端。垂直于对称轴的分量抵消，沿对称轴的分量相加：F = 2T cos30° = √3 kℓ。'],
  'T = k(2ℓ − ℓ) = kℓ；F = 2T cos30° = √3 kℓ',
  '弦的张力与弦对箭的合力是两个不同的量。', (540,347,240,245), '弓两端跨度为 ℓ，弦在中点被拉开，弦总长为 2ℓ。')

q(8,2,2,'已知合力与一个分力的方向',
  '已知两个共点力的合力为 60 N，分力 F₁ 的方向与合力 F 的方向成 30° 角，F₂ 的大小为 40 N，则（　）。',
  ['F₁ 的大小是唯一的','F₂ 的方向是唯一的','F₂ 有两个可能的方向','F₂ 可取任意方向'], 'C',[
  '以合力 F 为基准，将 F 分解到 F₁ 的方向及其垂直方向。垂直于 F₁ 的分量必须完全由 F₂ 提供，其大小为 60 sin30° = 30 N。',
  'F₂ 的大小为 40 N，因此它沿 F₁ 方向的分量可取 ±√(40² − 30²) = ±10√7 N。',
  '相应地，F₁ = 60 cos30° ∓ 10√7 = 30√3 ∓ 10√7 N。两值约为 25.5 N 和 78.4 N，均为正，因此都满足给定方向。',
  '两个有效的 F₁ 分别对应两个不同方向的 F₂，故只有 C 正确。'],
  'F₁ = 30√3 ± 10√7 N；F sin30° = 30 N < F₂ = 40 N < F = 60 N',
  '先检查几何解是否对应正的力大小，不能见到圆与直线就直接说有两个解。')

q(8,3,2,'旋转一个力后的合力范围',
  '如图所示，物体在五个共点力的作用下保持平衡，其中 F₁ 大小为 10 N。如果绕作用点旋转力 F₁，而保持其余四个力大小、方向都不变，那么这五个力的合力的大小可能为（　）。',
  ['30 N','21 N','14 N','7 N'], 'C、D',[
  '初态五力平衡，所以其余四个力的合力 R = −F₁，大小为 10 N，方向与原来的 F₁ 相反。',
  '旋转后 F₁′ 大小仍为 10 N，新的总合力为 R + F₁′。问题转化为两个大小均为 10 N 的力的合成。',
  '两力合力大小在 |10 − 10| 与 10 + 10 之间，即 0 至 20 N。14 N 和 7 N 可以出现，30 N 和 21 N 不可能。'],
  'F_合 = |F₁′ − F₁|；0 ≤ F_合 ≤ 20 N',
  '其余四力的合力并不为零，而是抵消原来的 F₁。', (470,870,400,280), '物体受五个共点力平衡，其中 F₁ 可绕作用点旋转。')

q(8,4,2,'斜面与挡板的支持力',
  '重为 G 的球，置于倾角为 α 的光滑斜面上，下方用垂直斜面的光滑挡板挡住使球静止，受力分析如图所示。\n（1）求斜面对球的支持力 F_N1 和挡板对球的支持力 F_N2。\n（2）若挡板竖直放置，斜面对球的支持力和挡板对球的支持力分别为多少？',
  [], '（1）G cosα、G sinα；（2）G/cosα、G tanα',[
  '（1）所有接触面光滑，支持力都垂直接触面。挡板垂直斜面时，挡板支持力沿斜面向上，斜面支持力垂直斜面向上。',
  '将重力分解到沿斜面和垂直斜面的方向：沿斜面分量为 G sinα，垂直斜面分量为 G cosα。平衡得到 F_N2 = G sinα、F_N1 = G cosα。',
  '（2）挡板改为竖直后，挡板支持力改为水平向右；斜面支持力仍垂直斜面。',
  '竖直方向只有斜面支持力的分量平衡重力：F_N1 cosα = G，故 F_N1 = G/cosα。水平方向 F_N2 = F_N1 sinα = G tanα。'],
  '挡板⊥斜面：F_N1 = G cosα，F_N2 = G sinα\n挡板竖直：F_N1 = G/cosα，F_N2 = G tanα',
  '挡板方向改变，支持力方向也改变，必须重新列平衡方程。', (120,1300,370,245), '小球由光滑斜面和垂直斜面的挡板支撑，斜面倾角为 α。')

q(8,5,3,'两根绳谁先断',
  '如图所示，轻质细绳 AO 和 BO 相交于 O 点，其 A、B 端是固定的，在 O 点用轻质细绳悬挂质量为 m 的物体。平衡时 AO 水平，BO 与水平方向的夹角为 θ。已知细绳 AO 和 BO 能承受的最大拉力相同，AO 和 BO 的拉力大小分别为 F₁ 和 F₂，重力加速度为 g，则（　）。',
  ['F₁ = mg tanθ','F₂ = mg/sinθ','F₁ 与 F₂ 的合力大小为 mg，方向竖直向下','增大物体的质量，最先断的是细绳 BO'], 'B、D',[
  '对结点 O 受力分析：AO 绳向左拉，BO 绳斜向右上拉，下方绳竖直向下拉且拉力为 mg。',
  '竖直方向平衡：F₂ sinθ = mg，所以 F₂ = mg/sinθ，B 正确。',
  '水平方向平衡：F₁ = F₂ cosθ = mg cotθ，A 错误。F₁、F₂ 的合力竖直向上且大小为 mg，C 的方向错误。',
  '由于 0 < cosθ < 1，F₁ = F₂ cosθ < F₂。在最大承受拉力相同的前提下，增大 m 时 BO 先达到极限，D 正确。'],
  'F₂ = mg/sinθ；F₁ = mg cotθ；F₂ > F₁',
  '两根上方绳的合力向上，用来平衡下方物体的重力。', (140,285,220,180), 'AO 绳水平向左，BO 绳向右上方，与水平成 θ，下方悬挂质量 m。')

q(9,1,2,'光滑晾衣绳上的衣服',
  '如图所示，光滑、轻质、不可伸长的晾衣绳两端分别固定于竖直杆上的 a、b 两点，一质量为 m 的衣服静止悬挂于绳上某点；若在绳上另一点继续悬挂另一质量为 M 的衣服，已知 m < M，两衣架质量均可忽略不计，则最终两衣服在绳上的状态为（　）。选项的几何位置见下图。',
  ['图 A：两衣服分处绳上不同位置','图 B：两衣服分处绳上不同位置','图 C：两衣服合在一起，位于偏右处','图 D：两衣服合在一起，位于偏左处'], 'D',[
  '衣架与绳之间光滑，衣架可沿绳滑动。绳轻且无摩擦，静止时各段张力大小相等。',
  '先看一件衣服：衣架两侧等大的张力合力必须竖直向上，故两侧绳与竖直方向的夹角相等。',
  '若两件衣服分开，设三段绳依次为左、中、右段。对左衣架，水平平衡要求左、中段的水平张力大小相等；对右衣架同理。等张力使三段绳的倾角绝对值相等。左衣架要有向上的合力，中段需向右上倾斜；此时右衣架两侧绳的竖直分量相消，无法托住右衣服。因此分开不能平衡。',
  '两衣服最终滑到同一处，两外侧绳的倾角应相同。右端 b 高于左端 a，故右侧绳段更长，汇合点应靠左。在给定选项中对应 D。'],
  'T_左 = T_右；两侧绳的倾角相同；T_左 + T_右 的矢量和 = (m + M)g 向上',
  '“光滑”意味着衣架可滑动，不能把衣服的位置当作固定结点。', (110,345,800,475), '原题初始示意图及 A、B、C、D 四个最终状态选项；b 端高于 a 端。')

q(9,2,2,'缓慢爬上半球形屋顶',
  '我国 2007 年建成的国家大剧院外部呈椭球型。为了简化，将国家大剧院的屋顶近似为半球形。某警卫人员在执行特殊任务时，必须在屋顶上向上缓慢爬行，他在爬行的过程中屋顶对他的（　）。',
  ['支持力不变','支持力变小','摩擦力变小','摩擦力变大'], 'C',[
  '缓慢爬行可按准静态平衡处理。设人所在位置的局部切面与水平面夹角为 α。',
  '将重力分解到切向和法向，得到支持力 N = mg cosα，静摩擦力 f = mg sinα，摩擦力沿屋顶切面向上。',
  '沿半球屋顶向上靠近顶点时，局部坡度变缓，α 减小。所以 cosα 增大、sinα 减小，即支持力增大、摩擦力减小，选 C。'],
  'N = mg cosα ↑；f = mg sinα ↓（向上爬，α ↓）',
  '这里采用“缓慢”对应的准静态模型；不要凭爬行方向判断摩擦力大小。')

q(9,3,3,'转动木板时的动态平衡',
  '如图，一小球静止在竖直墙壁和木板之间。现将木板从图示位置沿顺时针方向缓慢旋转至水平位置，不计一切摩擦，则下列说法正确的是（　）。',
  ['小球对墙壁的压力变大，对木板的压力变小','小球对墙壁的压力变小，对木板的压力变大','小球对墙壁的压力变小，对木板的压力变小','小球对墙壁的压力变大，对木板的压力变大'], 'C',[
  '设木板与水平夹角为 α。球受重力 mg、墙的水平支持力 N_墙、木板垂直板面的支持力 N_板。',
  '竖直平衡：N_板 cosα = mg，得 N_板 = mg/cosα。水平平衡：N_墙 = N_板 sinα = mg tanα。',
  '顺时针转至水平时 α 减小到 0，所以 N_板 逐渐减小至 mg，N_墙 逐渐减小至 0。',
  '由牛顿第三定律，球对墙和板的压力大小分别等于对应支持力，因此两压力均减小，C 正确。'],
  'N_板 = mg/cosα；N_墙 = mg tanα',
  '板水平时墙压力降为零，而板的压力仍为 mg。', (580,245,190,220), '球夹在左侧竖直墙与倾斜木板之间，木板顺时针转向水平。')

q(9,4,3,'攀岩中的绳与轻杆',
  '如图甲所示，一名登山爱好者沿竖直崖壁向上攀爬。绳的一端固定于较高处 A 点，另一端拴在人的腰间 C 点（重心处）。将人简化为乙图：脚与崖壁接触点为 O，重力 G 集中于 C 点，OC 简化为轻杆，AC 为轻绳。已知 OC 长度不变，人向上攀爬过程中的某时刻 AOC 构成等边三角形，则（　）。',
  ['轻绳对人的拉力与人对轻绳的拉力是一对平衡力','在此时刻，轻绳对人的拉力大小等于 G','在虚线位置时，轻绳 AC 承受的拉力更小','在虚线位置时，OC 段承受的压力变大'], 'B、D',[
  '绳对人与人对绳的拉力作用在两个物体上，是相互作用力，不是平衡力，A 错误。',
  '等边三角形位置，绳与杆均与水平成 30°。对 C：绳拉力 T 向左上，杆支持力 P 向右上。水平平衡给 T = P；竖直平衡给 (T + P)sin30° = G，因此 T = P = G，B 正确。',
  '在任意位置，取 A 在 O 正上方，记 AO = h、OC = ℓ、AC = s。对 C 的水平和竖直分量列平衡，可得 P/G = ℓ/h，T/G = s/h（也可由力三角形与几何三角形相似得到）。',
  '图示虚线位置中 O 向上移动，AO 减小，而 OC 不变；因此 P = Gℓ/h 增大。图中 C 的虚线位置更低，AC 更长，所以 T = Gs/h 也增大。因此 C 错误、D 正确。'],
  '等边位置：T = P = G\n一般位置：P = G·OC/AO，T = G·AC/AO',
  '把轻杆视为仅沿杆方向受力的理想二力杆。判断虚线位置时要看图中的角度变化。', (475,825,420,262), '攀岩简化图：A 在墙上方，O 为脚部支点，OC 为轻杆，AC 为绳；实线三角形为等边三角形，虚线杆更接近水平。')

q(9,5,4,'用悬球测量风速',
  '气象研究小组用如图所示简易装置测定水平风速。在水平地面上竖直固定一根直杆，质量为 m 的薄空心塑料球用细线悬于杆顶端 O。当水平风吹来时，球在水平风力作用下飘起来。已知风力大小正比于风速，当风速 v₀ = 3 m/s 时，测得球平衡时细线与竖直方向的夹角 θ = 30°，重力加速度为 g，则（　）。',
  ['θ = 30° 时，细线拉力大小为 (2√3/3)mg','风速增大到某一值时，θ 可能等于 90°','细线拉力与风力的合力大小大于 mg','θ = 60° 时，风速为 9 m/s'], 'A、D',[
  '受力为重力 mg、细线张力 T 和水平风力 F。平衡方程为 T cosθ = mg、T sinθ = F。',
  'θ = 30° 时，T = mg/cos30° = (2√3/3)mg，A 正确。有限张力必须具有向上的分量，θ 不能等于 90°，B 错误。',
  '由整体平衡，张力与风力的合力恰好为竖直向上的 mg，C 错误。',
  '两平衡方程相除得 F = mg tanθ。题设 F = kv，所以 v/v₀ = tanθ/tan30°。θ = 60° 时 v = 3 × √3/(1/√3) = 9 m/s，D 正确。'],
  'T = mg/cosθ；F = mg tanθ；v = 3·tanθ/tan30° m/s',
  '按题设风力与风速成正比，不能改成与风速平方成正比。', (125,282,180,195), '塑料球被水平风吹向右侧，细线与竖直方向成 θ。')

q(10,1,2,'牛顿定律与参考系',
  '1687 年，英国物理学家艾萨克·牛顿在伽利略、惠更斯等人关于动力学的一些观点的基础上，总结整理出三条描述力和运动关系的基本定律——牛顿运动定律，发表在《自然哲学的数学原理》一书中，为后来物理学很多领域的发展奠定了坚实可靠的基础。在宏观、低速、弱引力情况下，牛顿运动定律对物体的运动都能给出很好的解释或预测。关于牛顿运动定律，下列说法正确的是（　）。',
  ['牛顿第一定律说明力是维持物体运动的原因','若作用在运动物体上的力消失，则因为惯性，物体的加速度要隔一段时间才会消失','火车内静坐的乘客看到车内桌上的苹果在没有任何人碰的情况下突然朝自己滚来，在他看来，苹果的突然运动不能用牛顿第二定律解释','根据牛顿第三定律，一本静止于水平桌面上的书受到的重力和支持力一定大小相等、方向相反、作用在同一直线上'], 'C（以车厢为参考系，直接使用 F_合 = ma 时）',[
  '牛顿第一定律说明物体在不受外力或合力为零时保持静止或匀速直线运动。力是改变运动状态的原因，A 错误。',
  '由 a = F_合/m，合力消失时加速度立即变为零；速度不会因此突变。惯性不是加速度延迟消失的原因，B 错误。',
  '苹果相对车厢突然运动，说明车厢可能正在加速或减速。车厢为非惯性参考系，若只计真实力，不能直接套用 F_合 = ma 解释相对车厢的加速度，故按本题意 C 正确。',
  '静止书的重力与支持力确实平衡，但该结论来自平衡条件，不是牛顿第三定律。支持力的反作用力是书对桌面的压力，重力的反作用力是书对地球的引力，D 错误。'],
  '惯性系：ΣF_真实 = ma\n合力为零 → a = 0；v 保持不变',
  'C 的表述有省略：在车厢系中加入惯性力后仍可列动力学方程；换到地面惯性系也能解释。')

q(10,2,2,'角动量的国际单位',
  '陀螺仪的工作原理中常用到角动量的概念，角动量的大小为 L = rmv sinθ，其中 L 是质点的角动量，r 是质点到旋转轴的距离，m 是质点的质量，v 是质点的速度大小，θ 是 r 与 v 的夹角，则角动量用国际制基本单位表示为（　）。',
  ['kg·m²/s','kg·m/s','N·m/s','N·m·s'], 'A',[
  '从公式 L = rmv sinθ 出发，sinθ 为无量纲量，不影响单位。',
  'r 的单位为 m，质量 m 的单位为 kg，速度 v 的单位为 m/s。相乘得到 kg·m²/s。',
  'D 的 N·m·s 换算后也等于 kg·m²/s，但 N 为导出单位；题目要求用国际制基本单位表示，因此选 A。'],
  '[L] = m × kg × (m/s) = kg·m²·s⁻¹',
  '“单位等价”和“用基本单位表示”是两个不同要求。')

q(10,3,2,'剪断细线瞬间的加速度',
  '如图所示，质量均为 m 的 A、B 两球用轻弹簧连接，A 球用细线悬挂起来，两球均处于静止状态。如果将悬挂 A 球的细线剪断，此时 A、B 两球的瞬时加速度为（　）。',
  ['a_A 为 2g，a_B 为 0','a_A 和 a_B 均为 g','a_A 为 0，a_B 为 2g','a_A 和 a_B 均为 g/2'], 'A；A 球加速度竖直向下',[
  '剪断前 B 球平衡，弹簧对 B 的拉力向上，大小为 mg。弹簧对 A 的拉力向下，大小也为 mg。',
  '剪断瞬间弹簧长度来不及改变，因此弹簧弹力仍为 mg；上方细线的拉力则立即消失。',
  'A 球受到向下的重力 mg 与弹簧拉力 mg，合力为 2mg，故 a_A = 2g，方向向下。',
  'B 球的重力和弹簧拉力仍相互抵消，瞬时合力为零，所以 a_B = 0。'],
  'a_A = (mg + mg)/m = 2g ↓；a_B = (mg − mg)/m = 0',
  '弹簧弹力由形变量决定，瞬间保持不变；不可把两球立即当成一起自由落体。', (590,980,160,270), 'A 球由上方细线悬挂，B 球通过弹簧悬在 A 下方。')

q(10,4,3,'撤去拉力后的运动',
  '如图所示，质量 m = 2 kg 的物体静止于水平面上，现用一水平向右的恒力 F = 14 N 拉物体，物体运动 9 m 后撤去拉力 F。已知物体与水平面之间的动摩擦因数 μ = 0.5，g 取 10 m/s²。求：\n（1）物体在恒力作用下运动时的加速度大小 a；\n（2）撤去外力时速度大小 v；\n（3）撤去外力后，物体继续移动的位移大小 x。',
  [], '（1）2 m/s²；（2）6 m/s；（3）3.6 m',[
  '竖直方向平衡，N = mg = 20 N；滑动摩擦力 f = μmg = 0.5 × 2 × 10 = 10 N。',
  '（1）受拉力阶段：F − f = ma，得 a = (14 − 10)/2 = 2 m/s²。',
  '（2）从静止出发运动 9 m：v² = 2as = 2 × 2 × 9 = 36，得 v = 6 m/s。',
  '（3）撤去拉力后，摩擦力不变，减速度大小 a₂ = f/m = 5 m/s²。由 0 − v² = −2a₂x，得 x = 36/10 = 3.6 m。停止后摩擦力变为零，物体不会反向运动。'],
  'a₁ = (F − μmg)/m = 2 m/s²\nv = √(2a₁s) = 6 m/s\nx = v²/(2μg) = 3.6 m',
  '撤力只改变加速度，速度在撤力瞬间连续。', (510,238,240,80), '水平面上的物体受向右的恒力 F。')

q(10,5,3,'斜面与水平面的两段运动',
  '如图所示，AB 为某滑雪场的一条长直滑道，BC 为水平滑道，B 处与水平滑道平滑连接。AB 滑道倾角 θ = 37°，一质量 m = 15 kg 的雪橇（可视为质点）从 A 点由静止开始匀加速下滑到 B 点，到达 B 点时速度为 20 m/s，雪橇最后停止于 C 点。雪橇与 AB、BC 间的动摩擦因数相同，均为 μ = 0.25。取 g = 10 m/s²，sin37° = 0.6，cos37° = 0.8。\n（1）求斜面 AB 的长度；\n（2）求雪橇从 A 处开始运动到停止所经历的时间。',
  [], '（1）50 m；（2）13 s',[
  '沿 AB 向下取正。支持力 N₁ = mg cos37°，摩擦力沿斜面向上。由牛顿第二定律 a₁ = g(sin37° − μcos37°) = 10(0.6 − 0.25 × 0.8) = 4 m/s²。',
  '（1）由 v_B² = 2a₁s_AB，得 s_AB = 20²/(2 × 4) = 50 m。',
  '在 AB 上运动时间 t₁ = v_B/a₁ = 20/4 = 5 s。',
  '进入 BC 后速度连续，初速度为 20 m/s。减速度大小 a₂ = μg = 2.5 m/s²，因此停止所需时间 t₂ = 20/2.5 = 8 s。',
  '（2）总时间 t = t₁ + t₂ = 5 + 8 = 13 s。'],
  'a_AB = 4 m/s²；AB = 50 m\na_BC = −2.5 m/s²；t_总 = 5 + 8 = 13 s',
  '斜面上 N = mg cosθ；水平面上 N = mg，两段摩擦力不同。', (510,600,350,125), '雪橇从倾斜滑道 AB 下滑，再沿水平滑道 BC 停止。')

q(11,1,2,'电梯中的超重与失重',
  '下列漫画描绘了超失重的现象。若图 a 表示电梯静止或者匀速运动的情形，那么图 b、图 c 分别表示电梯在如何运动，下列说法正确的是（　）。',
  ['图 b 可能表示电梯向上做减速运动','图 b 可能表示电梯向上做加速运动','图 c 可能表示电梯向上做加速运动','图 c 可能表示电梯向下做减速运动'], 'B',[
  '竖直向上为正，对电梯内物体有 N − mg = ma。因此 N > mg 时为超重，a 向上；N < mg 时为失重，a 向下。',
  '图 b 中物体被压扁，表示支持力变大，即超重。可能的运动是向上加速或向下减速，因此 B 正确，A 错误。',
  '图 c 中物体呈拉长、飘起的漫画形态，表示失重，可能向下加速或向上减速。C、D 都对应加速度向上，因此错误。'],
  '超重：N > mg，a ↑；失重：N < mg，a ↓',
  '超重、失重由加速度方向决定，不能只看运动方向。', (128,306,578,240), '漫画 a 为正常状态，b 被压扁，c 呈拉长飘起状态。')

q(11,2,2,'从加速度图像分析蹲起',
  'phyphox 软件可以利用智能手机内的多种传感器，帮助我们完成各种各样的物理实验。某同学打开软件中的加速度传感器，把手机水平托在手上并使屏幕朝上，从静止站立状态开始做下蹲和起立的动作。传感器记录了该过程中竖直方向（z 轴，竖直向上为正）的运动数据，如图所示，g = 9.8 m/s²，下列说法正确的是（　）。',
  ['0—2 s 内，速度方向发生了变化','0—4 s 内，该同学完成了两次完整的蹲起动作','下蹲过程中手机处于失重，起立过程中处于超重','若手机质量 200 g，蹲起过程中手机所受手的支持力最多不超过 3.5 N'], 'D',[
  '图中给的是线性加速度，静止时约为零。0—2 s 的主要变化是先 a < 0、再 a > 0：先向下加速，再向下减速到停下，完成下蹲。加速度换向不代表速度换向，A 错误。',
  '约 2—4 s 先 a > 0、再 a < 0，对应向上加速、向上减速，完成起立。所以 0—4 s 只完成一次完整的蹲起，B 错误。',
  '下蹲的前半段失重、后半段超重；起立的前半段超重、后半段失重。C 错误。',
  '由 N = m(g + a)，图中最大正加速度约 6—7 m/s²，显著小于 7.7 m/s²。以 7 m/s² 作上界估算，N_max ≲ 0.2(9.8 + 7) = 3.36 N < 3.5 N，D 正确。'],
  'v(t) = v₀ + ∫a dt；N = m(g + a)\nN ≤ 3.5 N ⇔ a ≤ 7.7 m/s²（m = 0.2 kg）',
  '图像存在测量噪声，应依据主要波形与面积理解动作；不能把加速度的正负直接当成速度的正负。', (128,876,500,236), '竖直线性加速度随时间的曲线：0 至 2 秒先负后正，2 至 4 秒先正后负，最大正值约 6 至 7 m/s²。')

q(11,3,3,'落到弹簧上的小球',
  '如图所示，一小球从某高处 A 点从静止开始自由落下，落到直立于地面的轻弹簧上。小球从 B 点开始压缩弹簧，到达最低点 C，然后被弹簧弹回，不计空气阻力。下列说法中正确的是（　）。',
  ['小球从 A 到 B 点前做自由落体运动，运动越来越快，加速度越来越大','小球速度最大时的位置在 B、C 之间','小球从 B 点下落到 C 点的过程中，一直处于超重状态','小球从 A 点下落到 C 点的过程中，先做匀加速运动后做匀减速运动'], 'B',[
  'A 到 B 前为自由落体，速度增大，但加速度恒为 g，A 错误。',
  '进入弹簧后，设压缩量 x，竖直向下为正：a = g − kx/m。开始 kx < mg，小球向下加速；达到 kx = mg 时，加速度为零，速度达到最大。',
  '随后 kx > mg，加速度向上，小球仍向下运动但开始减速，直到 C 点速度为零。因此最大速度出现在 B、C 之间，B 正确。',
  'B 到最大速度位置弹力小于重力，为失重；之后为超重，C 错误。接触弹簧后加速度随 x 改变，不是匀加速或匀减速，D 错误。'],
  'a = g − kx/m；v 最大 ⇔ a = 0 ⇔ x = mg/k',
  '最低点速度为零，但加速度一般不为零；速度最大点才是合力为零的位置。', (135,242,135,240), '小球从 A 自由下落，在 B 接触弹簧，压缩到最低点 C。')

q(11,4,3,'细绳承受极限与最大加速度',
  '如图所示，在光滑水平地面上放着通过一细绳连在一起的 A、B 两物体，m_A = 2 kg，m_B = 4 kg，细绳能承受的最大拉力为 8 N。为使它们尽快运动起来，且不致使细绳被拉断，所施外力的大小和方向为（　）。',
  ['8 N，水平方向左拉 B','8 N，水平方向右拉 A','24 N，水平方向左拉 B','24 N，水平方向右拉 A'], 'C',[
  '若向左拉 B，绳拉力负责使 A 加速。对 A：T = m_Aa，因此 a ≤ 8/2 = 4 m/s²。',
  '整体质量为 6 kg，最大外力 F = (m_A + m_B)a = 6 × 4 = 24 N，对应选项 C。',
  '若向右拉 A，绳拉力负责使 B 加速，a ≤ 8/4 = 2 m/s²，最大外力只能为 6 × 2 = 12 N。',
  '比较两种拉法：拉质量较大的 B 可使系统获得更大加速度。24 N 向右拉 A 时，T = 4 × (24/6) = 16 N，会拉断细绳。'],
  '拉 B：a_max = T_max/m_A = 4 m/s²；F_max = 24 N\n拉 A：a_max = T_max/m_B = 2 m/s²；F_max = 12 N',
  '外力与绳内拉力不相等，要对被绳带动的物体单独列式。', (465,770,540,70), '光滑地面上 B 在左，A 在右，两物体由水平细绳相连。')

q(11,5,3,'四物块与压力传感器',
  '水平地面上并排放置四个质量均为 m 的相同物块，每个物块与地面间的动摩擦因数均为 μ，且最大静摩擦力等于滑动摩擦力。物块 1、2 之间固定一个质量不计的压力传感器。t = 0 时，对物块 1 施加一水平力 F，下列说法正确的是（　）。',
  ['若四个物块均静止，则物块之间的弹力的比例从左往右依次为 3∶2∶1','若四个物块一起向右匀加速运动，则物块之间的弹力的比例从左往右依次为 3∶2∶1','若 F 随时间均匀变化，满足关系 F = kt，则在 t = μmg/k 时，压力传感器的示数 F₁ = μmg','若 F 随时间均匀变化，满足关系 F = kt，则在 t = 6μmg/k 时，四个物块的加速度为 0.5μg'], 'B、D',[
  '设相邻接触力依次为 P₁₂、P₂₃、P₃₄。静止时，各物块的静摩擦力会在 0 到 μmg 之间按需要取值；题设未给出各处静摩擦力，不能保证接触力的比例为 3∶2∶1，A 错误。',
  '一起向右匀加速时，每块受到的滑动摩擦力都为 μmg。分别对右侧 3 块、2 块、1 块列式：P₁₂ = 3m(a + μg)、P₂₃ = 2m(a + μg)、P₃₄ = m(a + μg)，比例为 3∶2∶1，B 正确。',
  't = μmg/k 时，F = μmg，小于整体最大静摩擦力 4μmg，系统尚未整体滑动。传感器示数取决于静摩擦分配，不能确定为 μmg，C 错误。若物块 1 的静摩擦力单独平衡 F，传感器示数可为零。',
  't = 6μmg/k 时，F = 6μmg > 4μmg，系统已滑动。对整体：F − 4μmg = 4ma，得 a = (6μmg − 4μmg)/(4m) = 0.5μg，D 正确。'],
  '运动时：a = F/(4m) − μg\nP₁₂ : P₂₃ : P₃₄ = 3 : 2 : 1\nF = 6μmg → a = 0.5μg',
  '静摩擦力不一定达到 μmg，不能把运动状态下的接触力比例直接套到静止状态。', (130,1090,350,75), '四个相同物块 1 至 4 从左到右排列，F 推动最左侧物块，1 与 2 之间装有压力传感器。')

def crop_image(item):
    if not item['crop']:
        return None
    path = WORK / 'figures' / (item['id'] + '-' + '-'.join(map(str,item['crop'])) + '.png')
    path.parent.mkdir(exist_ok=True)
    if not path.exists():
        source = next(ROOT.glob(f"第{item['lesson']}讲*.pdf"))
        x,y,w,h = item['crop']
        subprocess.run(['pdftoppm','-f',str(item['page']),'-singlefile','-scale-to','1800',
            '-png','-x',str(x),'-y',str(y),'-W',str(w),'-H',str(h),str(source),str(path.with_suffix(''))],check=True)
    return 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode()

for item in questions:
    translated = QUESTIONS_EN[item['id']]
    assert len(translated['options']) == len(item['options']), item['id']
    assert len(translated['steps']) == len(item['steps']), item['id']
    assert all(translated[key] for key in ('title', 'text', 'answer', 'formula', 'trap'))
    item['en'] = translated
    item['image'] = crop_image(item)
    item['source'] = next(ROOT.glob(f"第{item['lesson']}讲*.pdf")).name

(WORK/'questions.json').write_text(json.dumps(questions,ensure_ascii=False,indent=2),encoding='utf-8')

E = html.escape
cards = []
for lesson,title in LESSONS.items():
    items = [v for v in questions if v['lesson']==lesson]
    content = []
    for item in items:
        figure = ''
        if item['image']:
            figure = f'<figure><img src="{item["image"]}" alt="{E(item["alt"])}" loading="lazy" width="{item["crop"][2]}" height="{item["crop"][3]}"><figcaption>原题配图</figcaption></figure>'
        options = ''.join(f'<li><span class="option-letter">{chr(65+i)}</span><span>{E(v)}</span></li>' for i,v in enumerate(item['options']))
        steps = ''.join(f'<li>{E(v)}</li>' for v in item['steps'])
        paragraphs = ''.join(f'<p>{E(v)}</p>' for v in item['text'].split('\n'))
        search = E(' '.join([item['title'],item['text'],*item['options'],title]))
        content.append(f'''<article class="question" id="{item['id']}" data-search="{search}">
          <div class="question-meta"><span class="question-index">练习 {item['number']:02d}</span><span>原 PDF 第 {item['page']} 页</span></div>
          <h3>{E(item['title'])}</h3><div class="question-text">{paragraphs}</div>{figure}
          <ol class="options" aria-label="选项">{options}</ol>
          <details class="answer" id="answer-{item['id']}"><summary><span class="show-label">Show answer <span>查看分步解析</span></span><span class="hide-label">Hide answer <span>收起解析</span></span><span class="plus" aria-hidden="true">＋</span></summary>
            <div class="answer-body"><div class="result"><span>参考答案</span><strong>{E(item['answer'])}</strong></div>
            <h4>一步一步推导</h4><ol class="steps">{steps}</ol>
            <pre class="equation" data-copy tabindex="0" title="双击复制公式">{E(item['formula'])}</pre>
            <aside class="trap"><strong>易错提醒</strong><p>{E(item['trap'])}</p></aside></div>
          </details></article>''')
    cards.append(f'''<details class="section" id="lesson-{lesson}" open><summary class="lesson-heading"><span class="lesson-no">{lesson:02d}</span><span><small>第 {lesson} 讲 · 5 道练习</small><h2>{E(title)}</h2></span><span class="section-chevron" aria-hidden="true">⌄</span></summary><div class="lesson-content">{''.join(content)}</div></details>''')

toc = ''.join(f'<a href="#lesson-{n}" data-lesson="{n}"><span>{n:02d}</span><span>{E(title)}<small>5 道练习</small></span></a>' for n,title in LESSONS.items())
structure = [{k:v for k,v in item.items() if k not in ('image','crop')} for item in questions]
canonical = '''PART A — CANONICAL TUTORIAL (MARKDOWN)
A. 学习目标：完成第7至11讲的25道练习，先独立思考再展开答案。
B. 定义：弹力 F=kx；滑动摩擦 f=μN；静摩擦按平衡需要取值；合力为矢量和。
C. 适用条件：经典力学、理想轻绳与轻弹簧；缓慢过程按准静态；摩擦按题设模型。
D. 推导：逐题受力分析、列平衡或 ΣF=ma，再用运动学求解，完整步骤见下方结构数据。
E. 例题：25道原题按五讲组织，完整文字、数值、选项、原图与解答均在页面中。
F. 易错点：弹力大小与方向、静摩擦与滑动摩擦、速度与加速度、平衡力与相互作用力。
G. 解题策略：明确研究对象和参考系，画受力图，选轴列式，核对单位和运动状态。
H. 自检：特别注意第7讲第4题的初始运动状态、第10讲第1题的参考系，以及图像读数精度。
'''

document = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="高途高中物理第7至11讲：25道原题、原图及可展开的逐步解析，离线可用。">
<title>力与运动 · 高中物理练习与分步解析</title>
<style>
:root{--bg:#f5f5f0;--panel:#fff;--text:#202e31;--muted:#687779;--accent:#12675c;--border:#dce2dc;--soft:#edf5ef;--side:280px}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}body{margin:0;background:var(--bg);color:var(--text);font:16px/1.85 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}button,input,summary{font:inherit}button,a,summary{-webkit-tap-highlight-color:transparent}button,summary{cursor:pointer}button:focus-visible,a:focus-visible,summary:focus-visible,input:focus-visible,[tabindex]:focus-visible{outline:3px solid #d79737;outline-offset:4px}button{border:1px solid var(--border);border-radius:9px;background:#fff;color:var(--text);padding:8px 14px;font-size:13px;white-space:nowrap}button:hover{background:var(--soft);border-color:#93b4a4}a{color:inherit}summary{list-style:none}summary::-webkit-details-marker{display:none}[hidden]{display:none!important}
.sidebar{position:fixed;inset:0 auto 0 0;width:var(--side);background:#eef1e9;border-right:1px solid var(--border);padding:32px 23px;overflow:auto;z-index:30;display:flex;flex-direction:column}.brand{display:flex;align-items:center;gap:12px;text-decoration:none;font-size:17px;font-weight:750;line-height:1.4}.brand-mark{display:grid;place-items:center;background:var(--accent);color:#fff;width:39px;height:39px;border-radius:11px;font-size:22px}.brand small{display:block;font-size:10px;letter-spacing:2px;color:var(--muted);font-weight:600;margin-top:3px}.nav-label{font-size:11px;letter-spacing:2px;color:var(--muted);margin:38px 10px 12px}.toc{display:grid;gap:7px}.toc a{display:flex;gap:13px;padding:12px 10px;border-radius:10px;text-decoration:none;font-size:13px;font-weight:600;line-height:1.55;border:1px solid transparent}.toc a>span:first-child{color:var(--accent);font-size:13px;margin-top:2px;font-variant-numeric:tabular-nums}.toc a:hover,.toc a.active{background:white;border-color:var(--border)}.toc small{display:block;font-size:11px;color:var(--muted);font-weight:400;margin-top:3px}.side-bottom{margin-top:auto;padding:28px 9px 0;font-size:12px;color:var(--muted)}.progress-track{height:5px;background:#d9e2d6;border-radius:9px;margin:10px 0}.progress-track i{display:block;height:100%;width:0;background:var(--accent);border-radius:9px;transition:width .2s}.side-bottom p{font-size:11px;line-height:1.7;margin:12px 0 0}
.workspace{margin-left:var(--side)}.topbar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:10px;padding:13px 34px;background:#f5f5f0f5;backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}.topbar-title{color:var(--muted);font-size:12px;letter-spacing:1px;margin-right:auto}.menu-button{font-size:16px;padding:5px 11px}.toolbar{display:flex;gap:8px}.primary-button{background:var(--accent);border-color:var(--accent);color:#fff}.primary-button:hover{background:#0e524a;color:#fff}.main{max-width:1060px;margin:0 auto;padding:47px 50px 60px}.eyebrow{font-size:11px;letter-spacing:2.6px;font-weight:700;color:var(--accent);margin-bottom:10px}.hero h1{font-size:clamp(32px,4vw,46px);line-height:1.3;margin:0 0 15px;font-weight:730;letter-spacing:-1px}.hero-description{color:var(--muted);font-size:14px;max-width:640px;margin:0}.stats{display:flex;gap:32px;margin-top:27px;padding-bottom:28px;border-bottom:1px solid var(--border)}.stats div{display:flex;align-items:baseline;gap:7px}.stats strong{font-size:24px;font-weight:650;color:var(--accent)}.stats span{font-size:12px;color:var(--muted)}.search-row{display:flex;gap:13px;align-items:center;margin:24px 0 29px}.search-box{display:flex;align-items:center;gap:11px;flex:1;border:1px solid var(--border);border-radius:10px;background:#fff;padding:7px 13px}.search-box span{font-size:22px;color:var(--accent)}.search-box input{border:0;background:transparent;width:100%;font-size:13px;color:var(--text);padding:5px 0;outline:none}.search-count{font-size:12px;color:var(--muted);white-space:nowrap}.search-box:focus-within{outline:2px solid #92b8a5;outline-offset:2px}.print-choice{display:flex;align-items:center;gap:5px;font-size:12px;color:var(--muted);white-space:nowrap}.print-choice input{accent-color:var(--accent)}
.section{margin:0 0 35px}.lesson-heading{display:flex;align-items:center;gap:15px;padding:9px 0 20px}.lesson-no{font-size:27px;line-height:1.2;color:var(--accent);font-weight:600;letter-spacing:-1px}.lesson-heading small{color:var(--muted);font-size:11px;letter-spacing:1px}.lesson-heading h2{font-size:22px;line-height:1.5;margin:1px 0 0;font-weight:650}.section-chevron{margin-left:auto;color:var(--muted);transition:transform .2s}.section:not([open]) .section-chevron{transform:rotate(-90deg)}.question{border:1px solid var(--border);border-radius:15px;background:var(--panel);padding:25px 28px 0;margin-bottom:18px;overflow:hidden;scroll-margin-top:90px;box-shadow:0 2px 3px #273a2d02}.question-meta{display:flex;justify-content:space-between;gap:10px;align-items:center;font-size:10px;color:var(--muted);letter-spacing:.6px}.question-index{display:inline-block;color:var(--accent);background:var(--soft);border-radius:5px;padding:3px 9px;font-weight:700;font-size:11px}.question h3{font-size:19px;font-weight:650;margin:12px 0 13px;line-height:1.55}.question-text{font-size:14px;line-height:1.95}.question-text p{margin:7px 0}figure{text-align:center;margin:22px auto;max-width:100%}figure img{display:block;height:auto;max-width:100%;margin:0 auto;border-radius:4px}figcaption{font-size:10px;letter-spacing:1px;color:var(--muted);margin-top:5px}.options{display:grid;gap:8px;list-style:none;margin:20px 0 23px;padding:0;font-size:13px}.options:empty{display:none}.options li{display:flex;align-items:baseline;gap:10px;padding:8px 11px;background:#f7f8f5;border-radius:7px;line-height:1.75}.option-letter{flex:0 0 18px;color:var(--accent);font-size:12px;font-weight:700}.answer{margin:23px -28px 0;border-top:1px solid var(--border)}.answer>summary{display:flex;align-items:center;justify-content:space-between;padding:14px 28px;color:var(--accent);font-size:13px;font-weight:650;line-height:1.6}.answer>summary:hover{background:#f6faf6}.show-label>span,.hide-label>span{font-size:11px;font-weight:400;margin-left:9px;color:var(--muted)}.hide-label{display:none}.answer[open] .hide-label{display:inline}.answer[open] .show-label{display:none}.answer[open] .plus{transform:rotate(45deg)}.plus{font-size:20px;font-weight:400;transition:transform .15s}.answer-body{padding:6px 28px 28px}.result{padding:14px 17px;background:var(--soft);border-left:3px solid var(--accent);border-radius:0 7px 7px 0;margin:4px 0 22px}.result>span{display:block;color:var(--accent);font-size:10px;letter-spacing:1.4px;margin-bottom:4px}.result strong{font-size:16px;font-weight:650}.answer-body h4{font-size:13px;color:var(--accent);font-weight:650;letter-spacing:.5px;margin:16px 0}.steps{list-style:none;padding:0;margin:0;counter-reset:step}.steps li{counter-increment:step;position:relative;padding:0 0 18px 37px;font-size:13px;line-height:1.95}.steps li:before{content:counter(step,decimal-leading-zero);position:absolute;left:0;top:1px;color:var(--accent);background:var(--soft);font:600 11px/25px -apple-system,sans-serif;border-radius:50%;width:25px;height:25px;text-align:center}.equation{font:13px/1.9 ui-monospace,SFMono-Regular,Consolas,"PingFang SC",monospace;white-space:pre-wrap;overflow-wrap:anywhere;padding:15px 18px;border:1px solid var(--border);background:#f7f8f5;border-radius:8px;margin:4px 0 20px}.trap{background:#fcf8ee;border:1px solid #efe3c6;border-radius:8px;padding:12px 16px;font-size:12px;color:#79612b}.trap strong{font-size:11px;letter-spacing:1px}.trap p{margin:4px 0 0}.empty{padding:50px 20px;text-align:center;border:1px dashed var(--border);border-radius:12px;color:var(--muted)}footer{font-size:11px;color:var(--muted);padding-top:15px;border-top:1px solid var(--border)}footer p{margin:8px 0}.hl h3{color:var(--accent)}.toast{position:fixed;bottom:25px;left:50%;transform:translateX(-50%);background:#203e36;color:white;border-radius:30px;padding:9px 20px;font-size:12px;z-index:60}.sidebar-hidden .sidebar{display:none}.sidebar-hidden .workspace{margin-left:0}.overlay{display:none}
.menu-panel{position:absolute;top:calc(100% + 8px);left:24px;width:260px;max-width:calc(100vw - 32px);background:var(--panel);border:1px solid var(--border);border-radius:13px;box-shadow:0 12px 36px #203e3626;padding:17px;z-index:40}.menu-panel h2{font-size:12px;line-height:1.5;letter-spacing:.7px;margin:0 0 12px;color:var(--muted);font-weight:600}.language-options{display:grid;grid-template-columns:1fr 1fr;gap:8px}.language-options button{font-size:13px;padding:8px}.language-options button[aria-pressed="true"]{background:var(--accent);color:white;border-color:var(--accent)}.browse-lessons{width:100%;margin-top:13px;font-size:12px;white-space:normal}.side-bottom p{white-space:pre-line}.toc a>span:last-child{min-width:0}.brand>span:last-child{min-width:0}html[lang="en"] .brand{font-size:15px}html[lang="en"] .brand small{font-size:9px;letter-spacing:1px}html[lang="en"] figcaption{max-width:650px;margin:10px auto 0;font-size:11px;line-height:1.7;letter-spacing:0;text-align:left}html[lang="en"] .hero h1{letter-spacing:-1.2px}.stats{flex-wrap:wrap}
@media(min-width:1500px){.main{max-width:1140px;padding-left:70px;padding-right:70px}}
@media(max-width:1100px){:root{--side:240px}.sidebar{padding:28px 16px}.main{padding:35px 28px}.topbar{padding:12px 22px}.topbar-title{display:none}.toolbar{margin-left:auto}.print-choice{display:none}}
@media(max-width:800px){:root{--side:260px}.sidebar{transform:translateX(-100%);transition:transform .2s}.workspace{margin-left:0}.sidebar-visible .sidebar{transform:translateX(0)}.sidebar-visible .overlay{display:block;position:fixed;inset:0;background:#152a274d;z-index:25}.sidebar-hidden .sidebar{display:flex}.topbar{gap:8px;padding:10px 16px}.toolbar{gap:6px}.toolbar button{font-size:11px;padding:7px 9px}.main{padding:30px 18px 45px}.eyebrow{font-size:9px}.hero h1{font-size:34px}.stats{gap:23px;margin-top:22px;padding-bottom:21px}.stats strong{font-size:21px}.stats span{font-size:11px}.search-row{margin:20px 0 24px;gap:8px}.search-count{font-size:10px}.search-box{padding:6px 10px}.search-box input{font-size:12px}.question{padding:20px 18px 0;border-radius:12px}.question h3{font-size:18px}.question-text{font-size:14px}.answer{margin-left:-18px;margin-right:-18px}.answer>summary{padding:13px 18px}.answer-body{padding:5px 18px 22px}.lesson-heading h2{font-size:20px}.lesson-no{font-size:24px}.show-label>span,.hide-label>span{font-size:10px;margin-left:6px}.question-meta{font-size:9px}.steps li{padding-left:34px}.result strong{font-size:14px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
@media(max-width:800px){.menu-panel{left:16px}html[lang="en"] .hero h1{font-size:32px}.stats{gap:16px}}
@media(max-width:380px){.topbar{padding-left:12px;padding-right:12px;gap:6px}.toolbar{gap:4px}.toolbar button{padding:7px 6px;font-size:10px}.menu-panel{left:12px}}
@media print{@page{margin:15mm}body{font-size:11pt;background:#fff;color:#111}.sidebar,.topbar,.search-row,.toast,.overlay,footer,.answer>summary,.section-chevron{display:none!important}.workspace{margin:0}.main{padding:0;max-width:none}.hero h1{font-size:26pt}.hero-description{font-size:10pt}.stats{margin:12px 0;padding-bottom:12px}.section{margin:20px 0}.lesson-heading{break-after:avoid;padding-bottom:10px}.question{border:1px solid #bbb;border-radius:6px;margin:10px 0;padding:14px 16px 0;box-shadow:none;overflow:visible}.question h3{font-size:13pt}.question-text,.options{font-size:10pt}.question-meta{font-size:8pt}figure{break-inside:avoid}figure img{max-height:80mm;width:auto;max-width:100%}.answer{margin-left:-16px;margin-right:-16px}.answer-body{padding:10px 16px}.steps li{font-size:9pt}.result,.trap,.equation{break-inside:avoid}.no-print-answers .answer{display:none}.question[hidden],.section[hidden]{display:none!important}}
</style></head><body>
<!--CANONICAL-->
<!-- PART B — STUDY PAGE STRUCTURE (JSON) -->
<script type="application/json" id="studyPageStructure">STRUCTURE</script>
<script type="application/json" id="lessonTranslations">LESSON_I18N</script>
<!-- PART C — FINAL HTML STUDY PAGE -->
<aside class="sidebar" id="sidebar" aria-label="章节导航"><a class="brand" href="#top"><span class="brand-mark">F</span><span>物理练习室<small>PHYSICS WORKBOOK</small></span></a><p class="nav-label">学习目录 / CONTENTS</p><nav class="toc">TOC</nav><div class="side-bottom"><span id="progressText">已查看 0 / 25 道解析</span><div class="progress-track" role="progressbar" aria-label="已查看解析进度" aria-valuemin="0" aria-valuemax="25" aria-valuenow="0"><i id="progressBar"></i></div><p>先独立作答，再展开解析。<br>公式框支持双击复制。<br>单文件 · 无需联网</p></div></aside>
<div class="overlay" id="overlay"></div><div class="workspace"><header class="topbar"><button type="button" class="menu-button" id="toggleSidebar" aria-label="打开语言与目录菜单" aria-controls="menuPanel" aria-expanded="false">☰</button><span class="topbar-title">高中物理 / 力与运动</span><div class="toolbar"><button type="button" class="primary-button" id="showAll">展开全部答案</button><button type="button" id="hideAll">收起全部答案</button><button type="button" id="print">打印 / PDF</button></div><label class="print-choice"><input type="checkbox" id="printAnswers" checked><span id="printLabel">打印含答案</span></label></header>
<main class="main" id="top"><section class="hero" aria-labelledby="pageTitle"><div class="eyebrow">高途高中物理 · 第 7—11 讲</div><h1 id="pageTitle">把每一步，想明白。</h1><p class="hero-description">从常见力到牛顿第二定律，整理原题与配图。点击每题下方的 Show answer，查看受力分析、分步推导与易错提醒。</p><div class="stats"><div><strong>05</strong><span>个专题</span></div><div><strong>25</strong><span>道练习</span></div><div><strong>25</strong><span>份分步解析</span></div></div></section>
<div class="search-row"><label class="search-box"><span aria-hidden="true">⌕</span><input type="search" id="search" aria-label="搜索题目或知识点" placeholder="搜索题目或知识点，如：弹簧、摩擦、加速度" autocomplete="off"></label><output id="searchCount" class="search-count" aria-live="polite">25 道题目</output></div>
<div id="lessons">CARDS</div><p class="empty" id="empty" hidden>没有找到匹配的题目，试试其他关键词。</p><footer><p>资料来源：本目录中的高途高中物理第 7—11 讲学生版 PDF。原题配图已嵌入，题目中的公式与数值已按页面图像核对。</p><p>参考答案与解析为重新推导，非原资料附带的官方答案。选择题可能有多个正确选项；存在条件歧义的题目已在解析中说明。</p></footer></main></div><div class="toast" id="toast" role="status" hidden></div>
<script>PAGE_SCRIPT</script></body></html>'''

document = document.replace('<!--CANONICAL-->','<!--\n'+canonical+'-->').replace('STRUCTURE',json.dumps(structure,ensure_ascii=False).replace('</','<\\/')).replace('TOC',toc).replace('CARDS',''.join(cards))
document = document.replace('LESSON_I18N', json.dumps({'zh': LESSONS, 'en': LESSONS_EN}, ensure_ascii=False)).replace('PAGE_SCRIPT', (WORK/'practice.js').read_text(encoding='utf-8'))
target=ROOT/'physics_practice.html'
target.write_text(document,encoding='utf-8')
print(f'Created {target.name}: {len(questions)} questions, {sum(bool(v["image"]) for v in questions)} embedded figures, {target.stat().st_size:,} bytes')
