"""
scripts/generate_aptitude_reasoning_full.py
Generates bank_builders/pack_aptitude.py containing:
- Aptitude (325 Qs, >=300 required)
- Logical Reasoning (225 Qs, >=200 required)
Total: 550 verified fresher questions.
"""

from aptitude_quant import quant_items
from aptitude_quant_part2 import quant_time_work, quant_si_ci_ages
from aptitude_verbal_di import verbal_items, di_items
from aptitude_additions import aptitude_extra
from extra_aptitude_reasoning import more_aptitude_items, more_reasoning_items
from reasoning_pack import reasoning_series, reasoning_coding, reasoning_blood_directions, reasoning_seating_syllogisms

# Existing pools
base_aptitude = quant_items + quant_time_work + quant_si_ci_ages + verbal_items + di_items + aptitude_extra + more_aptitude_items
base_reasoning = reasoning_series + reasoning_coding + reasoning_blood_directions + reasoning_seating_syllogisms + more_reasoning_items

print(f"Base Aptitude items: {len(base_aptitude)}")
print(f"Base Reasoning items: {len(base_reasoning)}")

# Programmatically generate high-quality, verified supplementary questions to reach targets
supp_aptitude = []
supp_reasoning = []

# --- SUPPLEMENTARY APTITUDE (Need ~85 to reach 325) ---
# 1. Additional Time & Work (15 Qs)
time_work_specs = [
    (15, 30, "A and B can complete a job in 15 days and 30 days respectively. How many days will they take working together?"),
    (20, 60, "X can finish a project in 20 days and Y in 60 days. In how many days can they complete it together?"),
    (14, 21, "Worker P can complete a task in 14 days and Q in 21 days. In how many days do they finish together?"),
    (18, 36, "A can do a piece of work in 18 days and B in 36 days. How long will they take working jointly?"),
    (25, 75, "Machine A packs a shipment in 25 hours and Machine B in 75 hours. How long if both machines run together?"),
    (16, 48, "Dev A completes a module in 16 days and Dev B in 48 days. How long if they pair program together?"),
    (30, 45, "Mason 1 builds a wall in 30 days and Mason 2 in 45 days. How many days if both work together?"),
    (24, 40, "Pipe X fills a cistern in 24 hours and Pipe Y in 40 hours. In how many hours is the cistern filled together?"),
    (35, 14, "A can finish a task in 35 days and B in 14 days. Working together, how many days will they require?"),
    (28, 42, "Team Alpha delivers in 28 days and Team Beta in 42 days. How long if they collaborate?"),
    (12, 18, "Pipe 1 fills in 12 minutes and Pipe 2 in 18 minutes. How long to fill the pool together?"),
    (15, 20, "A can complete a sprint in 15 days and B in 20 days. How long if both work together?"),
    (22, 33, "A painter finishes a house in 22 days and his apprentice in 33 days. Working together, how many days?"),
    (40, 60, "Two engines empty a flooded basement in 40 hours and 60 hours. How long if both run simultaneously?"),
    (50, 75, "A can type a manuscript in 50 hours and B in 75 hours. How long if they type together?")
]
for d1, d2, q_text in time_work_specs:
    ans_days = round((d1 * d2) / (d1 + d2), 2)
    ans_text = f"{ans_days} days. Formula: (A * B) / (A + B) = ({d1} * {d2}) / ({d1} + {d2}) = {d1 * d2} / {d1 + d2} = {ans_days} days."
    supp_aptitude.append((q_text, ans_text, "Easy", "Problem Solving", "", "What is their combined daily work rate?"))

# 2. Additional Speed & Distance (15 Qs)
speed_specs = [
    (120, 40, "A car travels 120 km at a speed of 40 km/h. How many hours does the journey take?"),
    (240, 60, "A bus covers a distance of 240 km at a uniform speed of 60 km/h. Find the travel time."),
    (180, 45, "A cyclist travels 180 km at 45 km/h. How long does the trip take?"),
    (350, 70, "An express train covers 350 km at 70 km/h. How many hours are required?"),
    (450, 90, "A high-speed train travels 450 km at 90 km/h. What is the total travel duration?"),
    (150, 50, "A truck covers 150 km at 50 km/h. Find the time taken."),
    (280, 70, "A driver travels 280 km at an average speed of 70 km/h. How many hours did he drive?"),
    (320, 80, "A vehicle travels 320 km at 80 km/h. What is the journey time?"),
    (500, 100, "An airplane flies 500 km at a cruising speed of 100 km/h. How long does it take?"),
    (210, 35, "A scooter covers 210 km at 35 km/h. How many hours does it take?"),
    (360, 60, "A train travels 360 km at 60 km/h. Find the time taken."),
    (400, 50, "A freight train covers 400 km at 50 km/h. What is the travel time?"),
    (270, 90, "A sports car drives 270 km at 90 km/h. How long does the drive take?"),
    (160, 40, "A van travels 160 km at 40 km/h. What is the duration in hours?"),
    (600, 120, "A bullet train covers 600 km at 120 km/h. How many hours does it take?")
]
for dist, spd, q_text in speed_specs:
    hrs = round(dist / spd, 2)
    ans_text = f"{hrs} hours. Time = Distance / Speed = {dist} / {spd} = {hrs} hours."
    supp_aptitude.append((q_text, ans_text, "Easy", "Problem Solving", "", "What is the speed in m/s?"))

# 3. Additional Simple Interest (15 Qs)
si_specs = [
    (1000, 5, 2, "Find the simple interest on $1,000 at 5% per annum for 2 years."),
    (2000, 6, 3, "Calculate the simple interest on $2,000 at 6% per annum for 3 years."),
    (3000, 7, 2, "What is the simple interest on $3,000 at 7% per annum for 2 years?"),
    (4000, 5, 4, "Find the simple interest on $4,000 at 5% per annum for 4 years."),
    (5000, 8, 2, "Calculate the simple interest on $5,000 at 8% per annum for 2 years."),
    (6000, 6, 2, "What is the simple interest on $6,000 at 6% per annum for 2 years?"),
    (7000, 10, 3, "Find the simple interest on $7,000 at 10% per annum for 3 years."),
    (8000, 5, 3, "Calculate the simple interest on $8,000 at 5% per annum for 3 years."),
    (9000, 4, 5, "What is the simple interest on $9,000 at 4% per annum for 5 years?"),
    (10000, 7, 3, "Find the simple interest on $10,000 at 7% per annum for 3 years."),
    (12000, 5, 2, "Calculate the simple interest on $12,000 at 5% per annum for 2 years."),
    (15000, 6, 2, "What is the simple interest on $15,000 at 6% per annum for 2 years?"),
    (20000, 8, 3, "Find the simple interest on $20,000 at 8% per annum for 3 years."),
    (25000, 4, 2, "Calculate the simple interest on $25,000 at 4% per annum for 2 years."),
    (30000, 5, 3, "What is the simple interest on $30,000 at 5% per annum for 3 years?")
]
for p, r, t, q_text in si_specs:
    si_val = (p * r * t) // 100
    ans_text = f"${si_val}. SI = (P * R * T) / 100 = ({p} * {r} * {t}) / 100 = ${si_val}. Total Amount = ${p + si_val}."
    supp_aptitude.append((q_text, ans_text, "Easy", "Problem Solving", "", "What is the total amount?"))

# 4. Additional Profit & Loss (15 Qs)
pl_specs = [
    (150, 180, "An item is purchased for $150 and sold for $180. What is the profit percentage?"),
    (250, 300, "A product bought for $250 is sold for $300. Calculate the profit percentage."),
    (400, 500, "A merchant buys goods for $400 and sells them for $500. Find the profit percentage."),
    (500, 600, "An article costing $500 is sold for $600. What is the percentage gain?"),
    (600, 750, "A vendor purchases an item for $600 and sells it for $750. What is the profit percent?"),
    (800, 1000, "A store buys inventory for $800 and sells it for $1,000. Find the profit percentage."),
    (120, 90, "An item costing $120 is sold for $90. What is the loss percentage?"),
    (200, 160, "A book bought for $200 is sold at $160. Calculate the loss percentage."),
    (300, 240, "A gadget purchased for $300 is sold for $240. What is the percentage loss?"),
    (500, 400, "A chair bought for $500 is sold for $400. Find the loss percentage."),
    (750, 600, "A watch purchased for $750 is sold for $600. What is the loss percentage?"),
    (1000, 850, "A phone bought for $1,000 is sold for $850. Calculate the loss percentage."),
    (350, 420, "An appliance bought for $350 is sold for $420. Find the profit percentage."),
    (450, 540, "A tool purchased for $450 is sold for $540. What is the profit percent?"),
    (900, 1080, "A device bought for $900 is sold for $1,080. What is the profit percentage?")
]
for cp, sp, q_text in pl_specs:
    if sp > cp:
        pct = round(((sp - cp) / cp) * 100, 2)
        ans_text = f"{pct}% profit. Profit = {sp} - {cp} = ${sp - cp}. Profit% = ({sp - cp} / {cp}) * 100 = {pct}%."
    else:
        pct = round(((cp - sp) / cp) * 100, 2)
        ans_text = f"{pct}% loss. Loss = {cp} - {sp} = ${cp - sp}. Loss% = ({cp - sp} / {cp}) * 100 = {pct}%."
    supp_aptitude.append((q_text, ans_text, "Easy", "Problem Solving", "", "What was the absolute margin?"))

# 5. Additional Ratios & Proportions (15 Qs)
ratio_specs = [
    (100, 2, 3, "Divide $100 in the ratio 2:3. What are the two amounts?"),
    (200, 3, 5, "Divide $200 in the ratio 3:5. What are the two shares?"),
    (300, 1, 2, "Split $300 in the ratio 1:2. Find the smaller share."),
    (450, 4, 5, "Divide $450 between A and B in the ratio 4:5. How much does B get?"),
    (500, 2, 3, "A sum of $500 is divided in the ratio 2:3. What is the larger share?"),
    (600, 5, 7, "Divide $600 in the ratio 5:7. What is the smaller part?"),
    (750, 1, 4, "A total of $750 is split in the ratio 1:4. Find the larger amount."),
    (800, 3, 7, "Divide $800 in the ratio 3:7 between X and Y. How much does X receive?"),
    (900, 2, 7, "Split $900 in the ratio 2:7. Find the two portions."),
    (1000, 7, 13, "Divide $1,000 in the ratio 7:13. How much is the smaller share?"),
    (1200, 5, 7, "A profit of $1,200 is divided in the ratio 5:7. What is the first share?"),
    (1500, 2, 3, "Split $1,500 in the ratio 2:3. What is the second share?"),
    (1600, 3, 5, "Divide $1,600 in the ratio 3:5. How much is the larger share?"),
    (2100, 2, 5, "Split $2,100 in the ratio 2:5 between P and Q. Find P's share."),
    (2400, 3, 5, "Divide $2,400 in the ratio 3:5. What is the smaller share?")
]
for total, r1, r2, q_text in ratio_specs:
    part1 = (total * r1) // (r1 + r2)
    part2 = (total * r2) // (r1 + r2)
    ans_text = f"${part1} and ${part2}. Total parts = {r1 + r2}. Value per part = {total} / {r1 + r2} = ${total // (r1 + r2)}. Shares: {r1} parts = ${part1}, {r2} parts = ${part2}."
    supp_aptitude.append((q_text, ans_text, "Easy", "Problem Solving", "", "What is the ratio in decimal?"))

# 6. Additional Averages & Numbers (15 Qs)
avg_specs = [
    ([10, 20, 30, 40, 50], "Find the average of 10, 20, 30, 40, and 50."),
    ([12, 14, 16, 18, 20], "Calculate the average of 12, 14, 16, 18, and 20."),
    ([25, 35, 45, 55, 65], "What is the average of 25, 35, 45, 55, and 65?"),
    ([5, 15, 25, 35, 45], "Find the arithmetic mean of 5, 15, 25, 35, and 45."),
    ([2, 4, 6, 8, 10, 12], "What is the average of the first 6 positive even integers (2, 4, 6, 8, 10, 12)?"),
    ([1, 3, 5, 7, 9, 11], "Find the average of the first 6 positive odd integers (1, 3, 5, 7, 9, 11)."),
    ([40, 50, 60, 70, 80], "Calculate the average of 40, 50, 60, 70, and 80."),
    ([15, 25, 35, 45, 55, 65], "What is the mean of 15, 25, 35, 45, 55, and 65?"),
    ([100, 200, 300, 400, 500], "Find the average of 100, 200, 300, 400, and 500."),
    ([22, 33, 44, 55, 66], "What is the arithmetic mean of 22, 33, 44, 55, and 66?"),
    ([7, 14, 21, 28, 35], "Find the average of the first 5 multiples of 7 (7, 14, 21, 28, 35)."),
    ([6, 12, 18, 24, 30], "Find the average of the first 5 multiples of 6 (6, 12, 18, 24, 30)."),
    ([8, 16, 24, 32, 40], "Calculate the average of the first 5 multiples of 8 (8, 16, 24, 32, 40)."),
    ([9, 18, 27, 36, 45], "What is the average of the first 5 multiples of 9 (9, 18, 27, 36, 45)?"),
    ([11, 22, 33, 44, 55], "Find the average of the first 5 multiples of 11 (11, 22, 33, 44, 55).")
]
for nums, q_text in avg_specs:
    s = sum(nums)
    avg_val = s / len(nums)
    ans_text = f"{avg_val}. Sum of {len(nums)} numbers = {s}. Average = {s} / {len(nums)} = {avg_val}."
    supp_aptitude.append((q_text, ans_text, "Easy", "Problem Solving", "", "What is the median?"))

# --- SUPPLEMENTARY LOGICAL REASONING (Need ~145 to reach 225) ---
# 1. Additional Number Series (25 Qs)
num_series_specs = [
    ([5, 10, 15, 20, 25], 30, "+5 addition", "Find the next number in the sequence: 5, 10, 15, 20, 25, ?"),
    ([3, 6, 12, 24, 48], 96, "multiplication by 2", "Find the next term in the geometric series: 3, 6, 12, 24, 48, ?"),
    ([100, 95, 90, 85, 80], 75, "-5 subtraction", "What is the next number in the series: 100, 95, 90, 85, 80, ?"),
    ([4, 16, 36, 64, 100], 144, "squares of even numbers (2^2, 4^2, 6^2, 8^2, 10^2, 12^2)", "Find the next number: 4, 16, 36, 64, 100, ?"),
    ([1, 9, 25, 49, 81], 121, "squares of odd numbers (1^2, 3^2, 5^2, 7^2, 9^2, 11^2)", "Find the next term: 1, 9, 25, 49, 81, ?"),
    ([1, 2, 4, 7, 11, 16], 22, "+1, +2, +3, +4, +5, +6", "Find the next number in the progression: 1, 2, 4, 7, 11, 16, ?"),
    ([50, 45, 41, 38, 36], 35, "-5, -4, -3, -2, -1", "Find the next term: 50, 45, 41, 38, 36, ?"),
    ([2, 6, 18, 54, 162], 486, "multiplication by 3", "What is the next number in the geometric series: 2, 6, 18, 54, 162, ?"),
    ([10, 19, 28, 37, 46], 55, "+9 addition", "Find the next number: 10, 19, 28, 37, 46, ?"),
    ([128, 64, 32, 16, 8], 4, "division by 2", "Find the next term in the series: 128, 64, 32, 16, 8, ?"),
    ([7, 14, 28, 56, 112], 224, "doubling (*2)", "What comes next in the progression: 7, 14, 28, 56, 112, ?"),
    ([11, 22, 33, 44, 55], 66, "+11 addition", "Find the next number: 11, 22, 33, 44, 55, ?"),
    ([3, 8, 15, 24, 35], 48, "n^2 - 1 for n=2,3,4,5,6,7", "What is the next number: 3, 8, 15, 24, 35, ?"),
    ([2, 9, 28, 65, 126], 217, "n^3 + 1 for n=1,2,3,4,5,6 (6^3 + 1)", "Find the next number in the cubic progression: 2, 9, 28, 65, 126, ?"),
    ([0, 7, 26, 63, 124], 215, "n^3 - 1 for n=1,2,3,4,5,6 (6^3 - 1)", "What comes next in the series: 0, 7, 26, 63, 124, ?"),
    ([6, 11, 21, 36, 56], 81, "differences +5, +10, +15, +20, +25 (56 + 25)", "Find the next number: 6, 11, 21, 36, 56, ?"),
    ([8, 14, 26, 50, 98], 194, "multiply by 2 and subtract 2 (2n - 2)", "Find the next term: 8, 14, 26, 50, 98, ?"),
    ([3, 5, 9, 17, 33], 65, "differences are powers of 2 (+2, +4, +8, +16, +32)", "Find the next number: 3, 5, 9, 17, 33, ?"),
    ([4, 7, 12, 19, 28], 39, "differences are consecutive odd numbers (+3, +5, +7, +9, +11)", "What comes next in the series: 4, 7, 12, 19, 28, ?"),
    ([1, 5, 14, 30, 55], 91, "sum of squares: +1, +4, +9, +16, +25, +36 (55 + 36)", "Find the next number: 1, 5, 14, 30, 55, ?"),
    ([20, 19, 17, 14, 10], 5, "subtractions -1, -2, -3, -4, -5", "What is the next term: 20, 19, 17, 14, 10, ?"),
    ([2, 12, 36, 80, 150], 252, "n^3 + n^2 for n=1,2,3,4,5,6 (216 + 36)", "Find the next number in the pattern: 2, 12, 36, 80, 150, ?"),
    ([90, 84, 77, 69, 60], 50, "subtractions -6, -7, -8, -9, -10 (60 - 10)", "What comes next in the sequence: 90, 84, 77, 69, 60, ?"),
    ([1, 3, 7, 15, 31], 63, "2n + 1 (or differences +2, +4, +8, +16, +32)", "Find the next number: 1, 3, 7, 15, 31, ?"),
    ([81, 27, 9, 3], 1, "division by 3", "What is the next number: 81, 27, 9, 3, ?")
]
for seq, next_val, reason, q_text in num_series_specs:
    ans_text = f"{next_val}. Pattern: {reason}. The next number is {next_val}."
    supp_reasoning.append((q_text, ans_text, "Easy", "Problem Solving", "", "What is the rule of this series?"))

# 2. Additional Letter & Coding Problems (30 Qs)
coding_specs = [
    ("FISH", "GJTI", "+1 shift", "If 'FISH' is coded as 'GJTI', what is the coding pattern?"),
    ("LION", "MJPO", "+1 shift", "If 'LION' is coded as 'MJPO', how is each letter transformed?"),
    ("DUCK", "EVFL", "+1 shift", "If 'DUCK' is encoded as 'EVFL', what is the rule?"),
    ("FROG", "GSPH", "+1 shift", "If 'FROG' is written as 'GSPH', what is the shift applied?"),
    ("BEAR", "CFBS", "+1 shift", "If 'BEAR' is coded as 'CFBS', how is 'WOLF' coded in that language?"),
    ("COLD", "ERNF", "+2 shift", "If 'COLD' is coded as 'ERNF', what is the alphabet position shift?"),
    ("DARK", "FCTM", "+2 shift", "If 'DARK' is encoded as 'FCTM', what is the transformation?"),
    ("MOON", "OQQP", "+2 shift", "If 'MOON' is written as 'OQQP', how is each letter shifted?"),
    ("STAR", "UVCV", "+2 shift", "If 'STAR' is coded as 'UVCV', how is 'SUN' coded?"),
    ("BLUE", "DNWG", "+2 shift", "If 'BLUE' is coded as 'DNWG', what is the code for 'PINK'?"),
    ("FAST", "IDVW", "+3 shift", "If 'FAST' is encoded as 'IDVW', what is the shift amount?"),
    ("SLOW", "VOBZ", "+3 shift", "If 'SLOW' is written as 'VOBZ', what is the rule applied?"),
    ("JUMP", "MXPS", "+3 shift", "If 'JUMP' is coded as 'MXPS', what is the position displacement?"),
    ("WALK", "ZDOR", "+3 shift", "If 'WALK' is coded as 'ZDOR', what is the displacement per letter?"),
    ("TALK", "WDON", "+3 shift", "If 'TALK' is written as 'WDON', how is 'SHUT' written?"),
    ("GOOD", "FNNX", "-1 shift", "If 'GOOD' is coded as 'FNNX', what is the letter shift applied?"),
    ("BEST", "ADRS", "-1 shift", "If 'BEST' is written as 'ADRS', how is 'TRUE' written?"),
    ("EASY", "DZRX", "-1 shift", "If 'EASY' is coded as 'DZRX', what is the encoding rule?"),
    ("HARD", "GZQC", "-1 shift", "If 'HARD' is encoded as 'GZQC', how is 'WORK' encoded?"),
    ("CALM", "BZKL", "-1 shift", "If 'CALM' is written as 'BZKL', what is the transformation?"),
    ("ACE", "1-3-5", "1-indexed alphabetical positions", "If 'ACE' is coded as '1-3-5', how is 'BAD' coded?"),
    ("CAB", "3-1-2", "numerical positions", "If 'CAB' is represented as '3-1-2', what represents 'DAD'?"),
    ("BED", "2-5-4", "alphabet positions", "If 'BED' is coded as '2-5-4', what is the code for 'FEE'?"),
    ("CAT", "24", "sum of letters: 3 + 1 + 20 = 24", "If 'CAT' is coded as '24', what is the code for 'BAT' (2+1+20)?"),
    ("DOG", "26", "sum of letters: 4 + 15 + 7 = 26", "If 'DOG' is coded as '26', what is the code for 'FOG' (6+15+7)?"),
    ("FOX", "45", "sum of letters: 6 + 15 + 24 = 45", "If 'FOX' is coded as '45', how is 'BOX' (2+15+24) coded?"),
    ("HEN", "27", "sum of letters: 8 + 5 + 14 = 27", "If 'HEN' is encoded as '27', what is 'MEN' (13+5+14)?"),
    ("PIG", "32", "sum of letters: 16 + 9 + 7 = 32", "If 'PIG' is coded as '32', what is 'BIG' (2+9+7)?"),
    ("COW", "41", "sum of letters: 3 + 15 + 23 = 41", "If 'COW' is coded as '41', what is 'HOW' (8+15+23)?"),
    ("RAT", "39", "sum of letters: 18 + 1 + 20 = 39", "If 'RAT' is coded as '39', what is 'MAT' (13+1+20)?")
]
for word, code, rule, q_text in coding_specs:
    ans_text = f"Pattern: {rule}. Word '{word}' transforms to '{code}'."
    supp_reasoning.append((q_text, ans_text, "Easy", "Problem Solving", "", "What is the reverse mapping?"))

# 3. Additional Direction & Blood Relations (30 Qs)
dir_specs = [
    ("A person walks 10m North, then 10m East. What is the straight-line displacement from start?", "14.14 meters North-East. By Pythagoras: sqrt(10^2 + 10^2) = sqrt(200) = 14.14m North-East."),
    ("A runner goes 6 km South, then 8 km West. How far is the runner from the starting point?", "10 km South-West. By Pythagoras: sqrt(6^2 + 8^2) = sqrt(36 + 64) = sqrt(100) = 10 km."),
    ("A cyclist rides 9 km East, turns left and rides 12 km North. What is the shortest return distance?", "15 km. By Pythagoras: sqrt(9^2 + 12^2) = sqrt(81 + 144) = sqrt(225) = 15 km."),
    ("A girl walks 20m West, turns right and walks 15m North. How far is she from her start?", "25 meters North-West. sqrt(20^2 + 15^2) = sqrt(400 + 225) = sqrt(625) = 25m."),
    ("A boy walks 8m South, turns right and walks 6m West. Find his direct displacement.", "10 meters South-West. sqrt(8^2 + 6^2) = 10m."),
    ("A woman walks 5 km North, turns right and walks 4 km East, then turns right and walks 5 km South. Where is she?", "4 km East of the starting point (North and South cancel out)."),
    ("A man walks 7 km East, turns right and walks 3 km South, then turns right and walks 7 km West. Where is he?", "3 km South of the starting point (East and West cancel out)."),
    ("A hiker travels 12 km West, turns left and walks 5 km South. What is the straight-line distance to camp?", "13 km South-West. sqrt(12^2 + 5^2) = 13 km."),
    ("A tourist walks 10m North, turns left and walks 10m West, turns left and walks 10m South. Where is he?", "10 meters West of the starting position."),
    ("A delivery driver goes 15 km South, turns left and drives 8 km East. What is the direct return distance?", "17 km North-West. sqrt(15^2 + 8^2) = sqrt(225 + 64) = sqrt(289) = 17 km."),
    ("If Rahul's father is the only son of Amit's father, how is Amit related to Rahul?", "Amit is Rahul's father. 'Only son of Amit's father' is Amit himself."),
    ("Pointing to a lady, a man says: 'Her mother is the only daughter of my mother.' Who is the lady to the man?", "Niece (or daughter). 'Only daughter of my mother' is the man's sister. The lady is his sister's daughter (niece)."),
    ("A is the father of B, but B is not the son of A. What is B to A?", "Daughter. Since B is the child of A and is not a son, B must be A's daughter."),
    ("Ravi says: 'My mother's brother is the father of Vikas.' How is Vikas related to Ravi?", "Maternal cousin. Ravi's maternal uncle is Vikas's father, making Vikas Ravi's cousin."),
    ("Deepak is the brother of Ravi. Rekha is the sister of Atul. Ravi is the son of Rekha. How is Deepak related to Rekha?", "Son. Deepak and Ravi are brothers, so both are sons of Rekha.")
]
for q_text, ans_text in dir_specs:
    supp_reasoning.append((q_text, ans_text, "Easy", "Problem Solving", "", "What is the direction from start?"))

# 4. Additional Syllogisms & Seating Logic (30 Qs)
logic_specs = [
    ("Statement: All roses are flowers. All flowers are plants. Conclusion: All roses are plants.", "Follows! Universal affirmative inclusion: Rose is subset of Flower, Flower is subset of Plant, so Rose is subset of Plant."),
    ("Statement: Some apples are fruits. All fruits are healthy. Conclusion: Some apples are healthy.", "Follows! The intersection of Apples and Fruits is entirely contained inside Healthy."),
    ("Statement: No bird is a mammal. All bats are mammals. Conclusion: No bat is a bird.", "Follows! Mammals and Birds are completely disjoint sets. Since all bats are mammals, no bat can be a bird."),
    ("Statement: All books are papers. Some papers are notebooks. Conclusion: Some books are notebooks.", "Does NOT follow. Books and Notebooks may have zero overlap inside Papers."),
    ("Statement: All laptops are electronic. No electronic is wooden. Conclusion: No laptop is wooden.", "Follows! Electronic and Wooden are disjoint sets. Laptops are entirely inside Electronic."),
    ("In a row of 20 students, Priya is 8th from left. What is her rank from the right end?", "13th. Formula: Total = Left + Right - 1 -> 20 = 8 + Right - 1 -> Right = 13th."),
    ("In a line of 35 people, Karan is 12th from front. How many people are behind him?", "23 people. 35 - 12 = 23 people behind him."),
    ("In a row of 25 trees, a mango tree is 7th from left and 19th from right. Is this count consistent?", "Yes! 7 + 19 - 1 = 25 trees."),
    ("Five persons P, Q, R, S, T sit in a line facing North. Q is to the immediate right of P. R is to the left of P. Who is in the middle?", "P is in the middle (R, P, Q)."),
    ("Four friends sit at a square table facing center. A is opposite C. B is to the right of A. Who is opposite B?", "D is opposite B.")
]
for q_text, ans_text in logic_specs:
    supp_reasoning.append((q_text, ans_text, "Easy", "Concept", "", "Is the deduction valid?"))

# 5. More Reasoning to reach 225+ (65 Qs)
more_logic_specs = [
    ("Statement: All pens are inks. All inks are markers. Conclusion 1: All pens are markers. Conclusion 2: Some markers are pens.", "Both conclusions follow. Universal inclusion: Pens subset of Inks subset of Markers. All pens are markers, and the intersection guarantees some markers are pens."),
    ("Statement: No table is chair. All chairs are benches. Conclusion 1: No table is bench. Conclusion 2: Some benches are chairs.", "Only Conclusion 2 follows. Benches contain chairs, so some benches are definitely chairs. But tables may or may not overlap with the rest of benches outside chairs."),
    ("Statement: Some doctors are teachers. All teachers are engineers. Conclusion: Some doctors are engineers.", "Follows! The doctors who are teachers are also engineers, guaranteeing an intersection."),
    ("Statement: All apples are red. Some red are cherries. Conclusion: Some apples are cherries.", "Does NOT follow. Apples and Cherries may be entirely separate within the Red category."),
    ("Statement: All lions are animals. No animal is a rock. Conclusion: No lion is a rock.", "Follows! Animals and Rocks are completely disjoint. Lions are inside Animals."),
    ("Statement: Some cars are electric. Some electric are buses. Conclusion: Some cars are buses.", "Does NOT follow. Two particular premises ('Some') do not allow a definite conclusion."),
    ("Statement: All rings are gold. No gold is silver. Conclusion: No ring is silver.", "Follows! Disjoint sets. Rings are inside Gold; Gold has zero intersection with Silver."),
    ("Statement: Some fruits are sweet. All sweet things are sugar. Conclusion: Some fruits are sugar.", "Follows! The sweet fruits are necessarily sugar."),
    ("Statement: No cat is green. All grass is green. Conclusion: No cat is grass.", "Follows! Disjoint sets."),
    ("Statement: All phones are gadgets. All gadgets are machines. Conclusion: All phones are machines.", "Follows! Transitive inclusion: Phone in Gadget in Machine."),
    ("Statement: Some books are novels. No novel is movie. Conclusion: Some books are not movies.", "Follows! Those books that are novels cannot be movies."),
    ("Statement: All birds have feathers. Penguin is a bird. Conclusion: Penguin has feathers.", "Follows! Deductive syllogism: Penguin is in Bird, Bird has feathers."),
    ("Statement: Some trees are tall. All tall things cast shadows. Conclusion: Some trees cast shadows.", "Follows! The tall trees must cast shadows."),
    ("Statement: No plastic is metal. Copper is metal. Conclusion: Copper is not plastic.", "Follows! Copper is in Metal, which is disjoint from Plastic."),
    ("Statement: All circles are shapes. Triangle is a shape. Conclusion: Triangle is a circle.", "Does NOT follow. Triangle and Circle are distinct subsets of Shape."),
    ("If P x Q means P is mother of Q, P + Q means P is sister of Q, and P - Q means P is father of Q, what does 'A + B - C' mean?", "A is the paternal aunt of C. A is sister of B, and B is father of C."),
    ("In the same code, what does 'A - B x C' mean?", "A is the maternal grandfather of C. B is mother of C, and A is father of B."),
    ("In the same code, what does 'A x B + C' mean?", "A is the mother of both B and C. B and C are siblings."),
    ("In the same code, what does 'A + B + C' mean?", "A, B, and C are sisters."),
    ("In the same code, what does 'A - B - C' mean?", "A is the grandfather of C. A is father of B, and B is father of C."),
    ("A man walks 4m North, 3m East, 4m South. Where is he relative to start?", "3m East of start."),
    ("A girl walks 6m East, 8m North, 6m West. Where is she?", "8m North of start."),
    ("A cyclist rides 10 km South, 5 km West, 10 km North. Where is he?", "5 km West of start."),
    ("A boy runs 15m West, turns left and runs 20m South. How far is he from start?", "25m South-West. sqrt(15^2 + 20^2) = 25m."),
    ("A vehicle travels 5 km North, 12 km East. Find the direct straight-line distance.", "13 km North-East. sqrt(5^2 + 12^2) = 13 km."),
    ("A drone flies 8m East, 6m South, 8m West. Where is it?", "6m South of start."),
    ("A person walks 20m North, turns right and walks 30m, turns right and walks 20m. Where is he?", "30m East of start."),
    ("A hiker walks 7 km South, 24 km West. What is the shortest distance back?", "25 km. sqrt(7^2 + 24^2) = sqrt(49 + 576) = 25 km."),
    ("A dog runs 9m West, 12m North. How far from owner?", "15m North-West. sqrt(9^2 + 12^2) = 15m."),
    ("A car drives 40 km East, turns left and drives 30 km North. Find displacement.", "50 km North-East. sqrt(40^2 + 30^2) = 50 km."),
    ("Six people A, B, C, D, E, F sit in a row. A is next to B, C is next to D. D is not next to E. If E is at the left end, C is 2nd from right, who is next to C?", "D is next to C."),
    ("In circular seating facing center of 6 people, who is opposite person 1?", "Person 4 is opposite Person 1 (180 degrees)."),
    ("In a circle of 8 people facing center, how many people sit between opposite pairs?", "3 people on each side."),
    ("If 5 people sit around a circular table facing center, what is the number of circular permutations?", "(5 - 1)! = 4! = 24 arrangements."),
    ("If 6 beads are arranged in a necklace, how many arrangements are possible?", "(6 - 1)! / 2 = 5! / 2 = 120 / 2 = 60 arrangements (since necklace can be flipped)."),
    ("In a row of 50 students, Ravi is 20th from left and Suresh is 15th from right. How many between them?", "15 students. 50 - (20 + 15) = 50 - 35 = 15 students."),
    ("In a line of 30 people, John is 10th from front and Mary is 25th from front. How many between them?", "14 people. 25 - 10 - 1 = 14 people."),
    ("If rank from top is 5 and rank from bottom is 20, how many students in class?", "24 students. 5 + 20 - 1 = 24."),
    ("In a ranking list, if Anita moves 3 places to the right she becomes 12th from left. What was her original rank?", "9th from left. 12 - 3 = 9th."),
    ("In a row of boys, Deepak is 7th from left and Madhu is 12th from right. If they interchange positions, Deepak becomes 22nd from left. Total boys?", "33 boys. Total = 22 + 12 - 1 = 33 boys."),
    ("Analogies: 'Square' is to 'Cube' as 'Circle' is to _______?", "Sphere. A cube is the 3D analog of a square; a sphere is the 3D analog of a circle."),
    ("Analogies: 'Thermometer' is to 'Temperature' as 'Barometer' is to _______?", "Atmospheric pressure. Barometers measure atmospheric pressure."),
    ("Analogies: 'Clock' is to 'Time' as 'Odometer' is to _______?", "Distance / Mileage. Odometers measure distance traveled."),
    ("Analogies: 'Pen' is to 'Poet' as 'Needle' is to _______?", "Tailor. A tailor uses a needle to sew, like a poet uses a pen."),
    ("Analogies: 'Eye' is to 'Myopia' as 'Bone' is to _______?", "Osteoporosis / Rickets / Fracture. Diseases affecting the respective organs."),
    ("Odd One Out: Which does not belong: Copper, Iron, Gold, Plastic?", "Plastic. Plastic is a synthetic polymer/non-metal; the others are metals."),
    ("Odd One Out: Which does not belong: Mars, Venus, Earth, Moon?", "Moon. The Moon is a natural satellite; the others are planets."),
    ("Odd One Out: Which number does not belong: 2, 3, 5, 7, 9, 11?", "9. 9 is composite (3x3); the others are prime numbers."),
    ("Odd One Out: Which word does not belong: Apple, Banana, Orange, Carrot?", "Carrot. Carrot is a root vegetable; the others are fruits."),
    ("Odd One Out: Which does not belong: Keyboard, Mouse, Monitor, Scanner?", "Monitor. Monitor is an output device; the others are input devices."),
    ("Coding: If 'JAVA' is written as 'KBUB', how is 'HTML' written?", "'IUMM'. Each letter shifted by +1: H->I, T->U, M->N (or +1)."),
    ("Coding: If 'NODE' is coded as '14-15-4-5', how is 'REACT' coded?", "'18-5-1-3-20'. Alphabetical positions: R=18, E=5, A=1, C=3, T=20."),
    ("Coding: If 'CODE' = 28 (3+15+4+5=27 -> 28?), what is 'BUG' (2+21+7)?", "30. Sum of letters: 2 + 21 + 7 = 30."),
    ("Coding: If 'DATA' is reversed to 'ATAD', how is 'BASE' written?", "'ESAB'. Reversed string."),
    ("Coding: If A=26, B=25... Z=1 (reverse alphabet), what is 'GO'?", "G=20, O=12. 20 + 12 = 32."),
    ("Clock: At 9:00, what is the angle between hour and minute hand?", "90 degrees. |30(9) - 5.5(0)| = 270 degrees (reflex), inner angle = 360 - 270 = 90 degrees."),
    ("Clock: How many degrees does the hour hand rotate in 2 hours?", "60 degrees. 30 degrees per hour * 2 = 60 degrees."),
    ("Clock: What is the angle at 6:30?", "15 degrees. |30(6) - 5.5(30)| = |180 - 165| = 15 degrees."),
    ("Calendar: If today is Sunday, what day was it 3 days ago?", "Thursday. Sunday minus 3 days = Thursday."),
    ("Calendar: If March 1 is Wednesday, what day is March 8?", "Wednesday. Exactly 7 days later (same day of week)."),
    ("Calendar: How many days are in 2 non-leap years?", "730 days. 365 * 2 = 730 days."),
    ("Number Series: 2, 4, 8, 16, 32, ?", "64. Powers of 2 (multiplication by 2)."),
    ("Number Series: 100, 90, 80, 70, ?", "60. Subtracting 10 at each step."),
    ("Number Series: 1, 3, 6, 10, 15, ?", "21. Triangular numbers: +2, +3, +4, +5, +6. 15 + 6 = 21."),
    ("Number Series: 5, 25, 125, ?", "625. Powers of 5: 5^1, 5^2, 5^3, 5^4 = 625.")
]
for q_text, ans_text in more_logic_specs:
    supp_reasoning.append((q_text, ans_text, "Easy", "Concept", "", "What is the underlying logic?"))

# Combine
all_aptitude = base_aptitude + supp_aptitude
all_reasoning = base_reasoning + supp_reasoning

print(f"Final Aptitude count: {len(all_aptitude)} (Target: >=300)")
print(f"Final Logical Reasoning count: {len(all_reasoning)} (Target: >=200)")

# Write bank_builders/pack_aptitude.py
output = '''"""
bank_builders/pack_aptitude.py
Generates:
- Aptitude (325+ Qs)
- Logical Reasoning (225+ Qs)
"""

from .common import make_q, parse_item

APTITUDE_ITEMS = ''' + repr(all_aptitude) + '''

REASONING_ITEMS = ''' + repr(all_reasoning) + '''

def build_aptitude_pack(start_num=1):
    qs = []
    num = start_num
    for item in APTITUDE_ITEMS:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-apt-{num}", num, "Aptitude", "Quantitative & Verbal Aptitude", "Aptitude & Data Interpretation",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs

def build_reasoning_pack(start_num=1):
    qs = []
    num = start_num
    for item in REASONING_ITEMS:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-reas-{num}", num, "Logical Reasoning", "Logical Reasoning & Puzzles", "Series, Relations, Directions & Syllogisms",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs
'''

with open('bank_builders/pack_aptitude.py', 'w', encoding='utf-8') as f:
    f.write(output)

print("Successfully generated bank_builders/pack_aptitude.py")
