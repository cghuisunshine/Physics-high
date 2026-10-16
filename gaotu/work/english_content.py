"""English text for all exercises; quantities and answer choices match the Chinese edition."""

LESSONS_EN = {
    7: 'Common Forces and Force Analysis',
    8: 'Combining Forces and Equilibrium',
    9: 'Changing Equilibrium',
    10: "Newton’s Laws of Motion",
    11: "Applying Newton’s Second Law",
}

QUESTIONS_EN = {}

def en(key, title, text, options, answer, steps, formula, trap, alt=''):
    QUESTIONS_EN[key] = dict(title=title, text=text, options=options, answer=answer,
                            steps=steps, formula=formula, trap=trap, alt=alt)

en('l7-q1', 'From Compression to Extension',
   'Two identical blocks A and B, each of mass 1 kg, are connected by a light spring of spring constant 500 N/m, as shown. Both blocks are initially at rest. An upward force F slowly lifts block A until block B is just about to leave the horizontal floor. Take g = 10 m/s². How far does block A move during this process?',
   ['1 cm', '2 cm', '4 cm', '8 cm'], 'C: 4 cm', [
   'Initially, block A is in equilibrium. Its weight mg acts downward and the spring force acts upward. Thus kx₁ = mg, so the spring is initially compressed by x₁ = 10/500 m = 2 cm.',
   'When B is just about to leave the floor, the normal force on B becomes zero. The spring must now pull B upward: kx₂ = mg. Therefore the spring is extended by x₂ = 2 cm.',
   'B does not move before it lifts off. A rises by the total change in spring length, from 2 cm of compression to 2 cm of extension: Δh = x₁ + x₂ = 4 cm.'],
   'Δh = mg/k + mg/k = 2mg/k = 0.04 m',
   'Add the initial compression and final extension; do not subtract their magnitudes.',
   'Block A sits above B, which rests on the floor. A vertical spring connects them, and an upward force F lifts A.')

en('l7-q2', 'Spring Force: Magnitude and Direction',
   'The graph shows the magnitude of the elastic force versus the length of a light spring within its elastic limit. Which statements are correct?',
   ['The natural length of the spring is 6 cm.',
    'The spring constant is 10 N/m.',
    'The elastic force is the same when the spring lengths are 4 cm and 8 cm.',
    'If a pulling force of 0.5 N is applied to each end, the spring has an equilibrium length of 6.5 cm.'], 'A and D', [
   'The force is zero at ℓ = 6 cm, so the natural length is ℓ₀ = 6 cm. A is correct.',
   'At the point (8 cm, 2 N), the extension is 0.02 m. Hence k = 2/0.02 = 100 N/m. B is incorrect.',
   'Lengths of 4 cm and 8 cm represent compression and extension of 2 cm, respectively. The forces have equal magnitudes of 2 N, but opposite directions at a given end. They are not the same force vector. C is incorrect.',
   'A force of 0.5 N at each end produces a spring tension of 0.5 N. The extension is x = 0.5/100 m = 0.5 cm, giving a length of 6.5 cm. D is correct.'],
   'F = k|ℓ − ℓ₀|; k = 100 N/m; ℓ = 6 cm + 0.5 cm = 6.5 cm',
   'Elastic force is a vector: equal magnitudes do not imply equal forces. Do not add the pulling forces at the two ends.',
   'Force magnitude F (N) versus length ℓ (cm): F = 0 at 6 cm and F = 2 N at both 4 cm and 8 cm.')

en('l7-q3', 'Friction When a Board Is Pulled Out',
   'A sufficiently long board B lies on a horizontal floor, with block A on top. A light string connects A to a horizontal spring balance fixed on the right. A horizontal force F pulls B to the left. Once conditions are steady, the spring balance reads Fₜ. Which statement is correct?',
   ['The friction on A is static friction.',
    'Whatever the speed of B while it is sliding under A, the friction between A and B equals Fₜ.',
    'The friction between A and B increases when B accelerates to the left.',
    'The friction between A and B decreases when B slows down while moving left.'], 'B', [
   'The string holds A in place while B slides to the left. There is relative sliding at the contact, so A experiences kinetic friction to the left.',
   'A is in horizontal equilibrium. The rightward string tension balances the leftward friction: f = Fₜ.',
   'In the standard kinetic-friction model, f = μN = μm_Ag. With the surfaces and normal force unchanged, friction is independent of the speed and acceleration of B. B is correct; C and D are incorrect.'],
   'f = μN = μm_Ag = Fₜ',
   'Choice B applies while B continues sliding relative to A. Reassess the friction if the board stops.',
   'A fixed spring balance on the right holds block A while board B is pulled to the left underneath it.')

en('l7-q4', 'Identify the Type of Friction First',
   'A spring of negligible mass and natural length 10 cm is attached to a block of mass m = 2 kg on a horizontal surface. A horizontal force F pulls its other end. The coefficient of kinetic friction is 0.2, and maximum static friction equals kinetic friction. Take g = 10 m/s².\n(1) When the spring length is 12 cm, the block moves at constant velocity. Find the spring constant.\n(2) If the spring length is 11 cm, find the friction force.\n(3) If the spring length is 13 cm, find the friction force.',
   [], '(1) 200 N/m; (2) 2 N when loaded from rest; (3) 4 N', [
   'Vertical equilibrium gives N = mg = 20 N. Both kinetic friction and maximum static friction have magnitude μN = 0.2 × 20 = 4 N.',
   '(1) At constant velocity, the spring force is 4 N. Its extension is 12 − 10 = 2 cm = 0.02 m, so k = 4/0.02 = 200 N/m.',
   '(2) Using the usual interpretation that each part starts with the block at rest, a length of 11 cm gives a spring force of k × 0.01 = 2 N. This is below maximum static friction, so the block stays at rest and static friction is 2 N.',
   '(3) At 13 cm, the spring force is k × 0.03 = 6 N, exceeding maximum static friction. The block slides, so the friction is 4 N.'],
   'f_max = μmg = 4 N; k = 200 N/m; F_11 = 2 N; F_13 = 6 N',
   'Part (2) depends on the initial state. If the block is already sliding, its friction is 4 N. Spring length alone does not establish that friction is 2 N.',
   'A horizontal spring attached to a block on the floor is pulled rightward at its free end.')

en('l7-q5', 'Forces on a Magnet and a Notice',
   'A magnet holds a paper notice against a vertical iron noticeboard, as shown. Which statement is correct?',
   ['Four forces act on the paper.',
    'The friction force on the magnet acts vertically downward.',
    'The friction exerted on the paper by the board is greater than the weight of the paper.',
    'The magnet’s normal force on the paper and the board’s normal force on the paper form an action–reaction pair.'], 'C', [
   'Consider the magnet first. Its weight acts downward, so static friction from the paper must act upward to balance it. B is incorrect.',
   'By Newton’s third law, the magnet exerts downward friction on the paper, equal in magnitude to the magnet’s weight.',
   'Vertically, the paper experiences its own weight, downward friction from the magnet, and upward friction from the board. Thus f = W_paper + W_magnet > W_paper. C is correct.',
   'The paper also experiences two normal forces, one from each side, for five forces in total. A is incorrect. Both forces in D act on the paper, so they are not an action–reaction pair.'],
   'f_board→paper = W_paper + W_magnet',
   'An action–reaction pair acts on two different objects. In this model the magnet does not exert a direct magnetic force on the paper.',
   'Small magnets press paper notices against a vertical iron board.')

en('l8-q1', 'Combining the Tensions in a Bowstring',
   'The ends of an archery bow are separated by ℓ, and this separation stays constant as the bow is drawn. The smooth, uniform elastic string has natural length ℓ and spring constant k. At release, the arrow and its attached device are at the midpoint of the string, whose total length is 2ℓ. Assuming Hooke’s law applies, find the string tension ________ and the magnitude of the force exerted by the string on the arrow ________.',
   [], 'kℓ; √3 kℓ', [
   'The full string stretches from ℓ to 2ℓ, an extension of ℓ. Hooke’s law gives its tension T = kℓ.',
   'Since the arrow is at the midpoint, each half of the string has length ℓ. The separation of the bow’s ends is also ℓ. These three sides form an equilateral triangle, so the angle between the string segments at the arrow is 60°.',
   'Each segment pulls on the arrow with magnitude T toward its fixed end. Components perpendicular to the symmetry axis cancel, while components along the axis add: F = 2T cos30° = √3 kℓ.'],
   'T = k(2ℓ − ℓ) = kℓ; F = 2T cos30° = √3 kℓ',
   'The tension in the string and the resultant force on the arrow are different quantities.',
   'The bow’s end separation is ℓ. The arrow and attached device pull back the string at its midpoint; the full string length is 2ℓ. Original labels: bow, arrow, string, attached device.')

en('l8-q2', 'A Known Resultant and a Component Direction',
   'Two concurrent forces have a resultant F of magnitude 60 N. The direction of F₁ makes an angle of 30° with F, and F₂ has magnitude 40 N. Which statement is correct?',
   ['The magnitude of F₁ is unique.', 'The direction of F₂ is unique.',
    'F₂ has two possible directions.', 'F₂ can have any direction.'], 'C', [
   'Resolve the resultant parallel and perpendicular to F₁. The perpendicular component must come entirely from F₂ and has magnitude 60 sin30° = 30 N.',
   'Since |F₂| = 40 N, its component along F₁ can be ±√(40² − 30²) = ±10√7 N.',
   'Therefore F₁ = 60 cos30° ∓ 10√7 = 30√3 ∓ 10√7 N. The two values are about 25.5 N and 78.4 N. Both are positive and therefore consistent with the specified direction.',
   'These two valid magnitudes of F₁ correspond to two different directions of F₂. Only C is correct.'],
   'F₁ = 30√3 ± 10√7 N; F sin30° = 30 N < F₂ = 40 N < F = 60 N',
   'Check that each geometric solution gives a positive force magnitude in the specified direction.')

en('l8-q3', 'The Resultant After One Force Rotates',
   'An object is in equilibrium under five concurrent forces, as shown. F₁ has magnitude 10 N. If F₁ rotates about the point of application while the other four forces remain unchanged in magnitude and direction, which resultant magnitudes are possible?',
   ['30 N', '21 N', '14 N', '7 N'], 'C and D', [
   'Initially the five forces balance. The resultant R of the other four forces is therefore −F₁: it has magnitude 10 N and points opposite to the original F₁.',
   'After rotation, F₁′ still has magnitude 10 N. The new total force is R + F₁′, the sum of two forces of magnitude 10 N.',
   'Their resultant lies between |10 − 10| and 10 + 10, or 0 to 20 N. Thus 14 N and 7 N are possible; 30 N and 21 N are not.'],
   'F_net = |F₁′ − F₁|; 0 ≤ F_net ≤ 20 N',
   'The other four forces do not have zero resultant; they cancel the original F₁.',
   'Five concurrent forces keep the object in equilibrium. Force F₁ can rotate about their common point of application.')

en('l8-q4', 'Normal Forces from a Slope and a Stop',
   'A ball of weight G rests on a smooth slope inclined at angle α. A smooth stop perpendicular to the slope prevents the ball from sliding down, as shown.\n(1) Find the normal force F_N1 from the slope and F_N2 from the stop.\n(2) If the stop is instead vertical, find the two normal forces.',
   [], '(1) G cosα, G sinα; (2) G/cosα, G tanα', [
   '(1) All surfaces are smooth, so each contact force is perpendicular to its surface. With the stop perpendicular to the slope, its force acts up the slope, while the slope’s force is normal to the slope.',
   'Resolve the weight parallel and perpendicular to the slope: the components are G sinα and G cosα. Equilibrium gives F_N2 = G sinα and F_N1 = G cosα.',
   '(2) With a vertical stop, its normal force acts horizontally to the right. The slope’s normal force keeps its original direction.',
   'Vertical equilibrium gives F_N1 cosα = G, so F_N1 = G/cosα. Horizontal equilibrium then gives F_N2 = F_N1 sinα = G tanα.'],
   'Stop perpendicular to slope: F_N1 = G cosα, F_N2 = G sinα\nVertical stop: F_N1 = G/cosα, F_N2 = G tanα',
   'Changing the stop’s orientation changes the direction of its force. Write new equilibrium equations.',
   'A ball rests between a smooth incline at angle α and a stop perpendicular to the incline. The diagram labels the weight G and the two normal forces.')

en('l8-q5', 'Which String Breaks First?',
   'Light strings AO and BO meet at O, with their ends A and B fixed. A mass m hangs from O on another light string. In equilibrium, AO is horizontal and BO makes angle θ with the horizontal. AO and BO have the same maximum breaking tension. Their tensions are F₁ and F₂ respectively, and gravitational acceleration is g. Which statements are correct?',
   ['F₁ = mg tanθ', 'F₂ = mg/sinθ',
    'The resultant of F₁ and F₂ has magnitude mg and acts vertically downward.',
    'If the hanging mass increases, string BO breaks first.'], 'B and D', [
   'At junction O, AO pulls leftward, BO pulls upward and rightward, and the lower string pulls downward with tension mg.',
   'Vertical equilibrium gives F₂ sinθ = mg, so F₂ = mg/sinθ. B is correct.',
   'Horizontal equilibrium gives F₁ = F₂ cosθ = mg cotθ. A is incorrect. The resultant of F₁ and F₂ is upward with magnitude mg, so C has the wrong direction.',
   'Because 0 < cosθ < 1, F₁ = F₂ cosθ < F₂. With equal breaking tensions, BO reaches its limit first as m increases. D is correct.'],
   'F₂ = mg/sinθ; F₁ = mg cotθ; F₂ > F₁',
   'The resultant of the two upper string tensions acts upward to balance the hanging weight.',
   'AO extends horizontally left from O; BO extends up and right at angle θ to the horizontal. A mass m hangs below O.')

en('l9-q1', 'Clothes on a Smooth Clothesline',
   'A smooth, light, inextensible clothesline has its ends fixed at a and b on two vertical posts. A garment of mass m hangs at rest from one point on the line. A second garment of mass M is then hung from another point, where m < M. The hangers have negligible mass. Which diagram shows the final arrangement? The initial arrangement and choices A–D are shown below.',
   ['Diagram A: the garments remain at separate points.',
    'Diagram B: the garments remain at separate points.',
    'Diagram C: the garments meet at a point toward the right.',
    'Diagram D: the garments meet at a point toward the left.'], 'D', [
   'The hangers can slide along the smooth line. Because the line is light and the contacts are frictionless, all segments have equal tension in equilibrium.',
   'For a single loaded hanger, the two equal tensions must have an upward resultant. The string segments on its two sides therefore make equal angles with the vertical.',
   'If the garments were separate, horizontal equilibrium at both hangers would require all three string segments to have the same absolute inclination. To support the left garment, the middle segment would have to slope upward to the right. At the right garment, its two tension forces would then have cancelling vertical components and could not support its weight. A separated arrangement cannot be in equilibrium.',
   'The garments slide together. The two outer string segments must then have equal inclinations. Since b is higher than a, the right segment is longer, placing the meeting point toward the left. This is diagram D.'],
   'T_left = T_right; equal inclinations\nVector sum of the two tensions = (m + M)g upward',
   'A smooth contact allows the hangers to slide. Their initial positions are not fixed junctions.',
   'Initial arrangement above, followed by choices A–D. Endpoint b is higher than a. In D the garments meet toward the left with equally inclined outer segments.')

en('l9-q2', 'Climbing a Hemispherical Roof Slowly',
   'China’s National Centre for the Performing Arts, completed in 2007, has an ellipsoidal exterior. Model its roof as a hemisphere. A guard slowly climbs upward along the roof during a special task. As the guard climbs, which statement about the forces exerted by the roof is correct?',
   ['The normal force stays constant.', 'The normal force decreases.',
    'The friction force decreases.', 'The friction force increases.'], 'C', [
   'Treat the slow motion as quasi-static equilibrium. Let α be the angle between the local tangent to the roof and the horizontal.',
   'Resolve the weight in the tangential and normal directions. The normal force is N = mg cosα and static friction is f = mg sinα, directed up the local slope.',
   'The local slope becomes gentler as the guard approaches the top, so α decreases. Thus cosα increases while sinα decreases: the normal force increases and friction decreases. C is correct.'],
   'N = mg cosα increases; f = mg sinα decreases (α decreases uphill)',
   'Use the quasi-static approximation implied by “slowly.” The direction of motion alone does not determine the size of friction.')

en('l9-q3', 'A Slowly Rotating Support Board',
   'A ball is at rest between a vertical wall and an inclined board. The board slowly rotates clockwise from the position shown until it is horizontal. Ignore all friction. Which statement is correct?',
   ['The ball’s force on the wall increases and its force on the board decreases.',
    'The ball’s force on the wall decreases and its force on the board increases.',
    'The ball’s forces on both the wall and the board decrease.',
    'The ball’s forces on both the wall and the board increase.'], 'C', [
   'Let the board’s angle to the horizontal be α. The ball experiences weight mg, a horizontal normal force N_wall, and a force N_board perpendicular to the board.',
   'Vertical equilibrium gives N_board cosα = mg, so N_board = mg/cosα. Horizontal equilibrium gives N_wall = N_board sinα = mg tanα.',
   'As the board rotates clockwise to horizontal, α decreases to zero. N_board decreases to mg, and N_wall decreases to zero.',
   'By Newton’s third law, the ball’s forces on the wall and board have the same magnitudes as these respective normal forces. Both decrease, so C is correct.'],
   'N_board = mg/cosα; N_wall = mg tanα',
   'When the board is horizontal, the wall force is zero, but the board still supports the weight mg.',
   'A ball is held between a vertical wall on the left and an inclined board that rotates clockwise toward horizontal.')

en('l9-q4', 'A Climber, a Rope, and a Light Rod',
   'A climber ascends a vertical cliff, as shown in panel 甲 (a). A rope runs from a fixed high point A to the climber’s waist at C, the centre of mass. In the idealized model in panel 乙 (b), O is the foot contact, the weight G acts at C, OC is a light rod, and AC is a light rope. OC has constant length. At one instant triangle AOC is equilateral. Which statements are correct?',
   ['The rope’s force on the climber and the climber’s force on the rope form a balanced pair of forces.',
    'At this instant, the rope tension equals G.',
    'At the dashed position, the tension in AC is smaller.',
    'At the dashed position, the compressive force in OC is larger.'], 'B and D', [
   'The rope’s force on the climber and the climber’s force on the rope act on different objects. They are an action–reaction pair, not a balanced pair acting on one object. A is incorrect.',
   'In the equilateral position, both rope and rod make 30° with the horizontal. At C, tension T acts up and left and rod force P acts up and right. Horizontal equilibrium gives T = P; vertical equilibrium gives (T + P)sin30° = G. Hence T = P = G. B is correct.',
   'For a general position with A vertically above O, let AO = h, OC = ℓ, and AC = s. Resolving the two support forces gives P/G = ℓ/h and T/G = s/h. The same result follows from similar force and geometry triangles.',
   'At the dashed position, O has moved upward: AO decreases while OC remains fixed, so P = Gℓ/h increases. The dashed C is lower in the drawing, increasing AC; hence T = Gs/h also increases. C is incorrect and D is correct.'],
   'Equilateral position: T = P = G\nGeneral position: P = G·OC/AO; T = G·AC/AO',
   'Model OC as an ideal two-force rod: its force acts along the rod. Read the dashed geometry carefully.',
   'Panel 甲 (a): climber. Panel 乙 (b): A is the upper wall anchor, O the foot contact, OC the rod, and AC the rope. The solid triangle is equilateral; the dashed rod is closer to horizontal.')

en('l9-q5', 'Measuring Wind Speed with a Suspended Ball',
   'A weather research group measures horizontal wind speed using the device shown. A thin hollow plastic ball of mass m hangs by a string from the top O of a vertical pole. A horizontal wind deflects the ball. The wind force is directly proportional to wind speed. When v₀ = 3 m/s, the equilibrium string angle to the vertical is θ = 30°. Gravitational acceleration is g. Which statements are correct?',
   ['At θ = 30°, the string tension is (2√3/3)mg.',
    'At a sufficiently high finite wind speed, θ can equal 90°.',
    'The resultant of string tension and wind force is greater than mg.',
    'At θ = 60°, the wind speed is 9 m/s.'], 'A and D', [
   'The ball experiences weight mg, string tension T, and horizontal wind force F. Equilibrium gives T cosθ = mg and T sinθ = F.',
   'At 30°, T = mg/cos30° = (2√3/3)mg. A is correct. A finite tension must have an upward component, so θ cannot equal 90°. B is incorrect.',
   'In equilibrium, the resultant of tension and wind force is exactly mg vertically upward. C is incorrect.',
   'Dividing the equilibrium equations gives F = mg tanθ. Since the problem specifies F = kv, v/v₀ = tanθ/tan30°. At 60°, v = 3 × √3/(1/√3) = 9 m/s. D is correct.'],
   'T = mg/cosθ; F = mg tanθ; v = 3·tanθ/tan30° m/s',
   'Use the stated linear relation between wind force and wind speed; do not replace it with a square law.',
   'Horizontal wind blows rightward, deflecting the ball. The string from O makes angle θ with the vertical. The Chinese arrow label means “horizontal wind.”')

en('l10-q1', 'Newton’s Laws and Reference Frames',
   'In 1687, Isaac Newton built on ideas about dynamics developed by Galileo, Huygens, and others, and presented three laws relating force and motion in Mathematical Principles of Natural Philosophy. These laws established a foundation for many areas of physics. They describe and predict motion well for macroscopic objects at low speeds and in weak gravitational fields. Which statement about Newton’s laws is correct?',
   ['Newton’s first law states that force is needed to maintain motion.',
    'If the forces acting on a moving object disappear, its inertia makes its acceleration persist for a while before vanishing.',
    'A passenger seated in a train sees an untouched apple suddenly roll toward them on the table. From the passenger’s train-based viewpoint, this sudden motion cannot be explained by directly applying Newton’s second law using only real forces.',
    'By Newton’s third law, the weight and normal force on a book at rest on a horizontal table must have equal magnitudes, opposite directions, and a common line of action.'],
   'C, for direct application of F_net = ma in the train’s frame', [
   'Newton’s first law says an object remains at rest or in uniform straight-line motion when its net force is zero. Force changes motion; it is not required to maintain constant velocity. A is incorrect.',
   'From a = F_net/m, acceleration becomes zero as soon as the net force vanishes. Velocity does not suddenly vanish. Inertia does not delay the change in acceleration. B is incorrect.',
   'The apple’s sudden motion relative to the carriage suggests that the carriage is accelerating or decelerating. This is a non-inertial frame, so F_net = ma cannot be applied directly to the apple’s relative acceleration using only real forces. This is the intended meaning of C.',
   'The stationary book’s weight and normal force do balance, but this follows from equilibrium, not Newton’s third law. The reaction to the normal force is the book’s force on the table; the reaction to its weight is its gravitational pull on Earth. D is incorrect.'],
   'In an inertial frame: ΣF_real = ma\nZero net force → a = 0; velocity remains constant',
   'Choice C needs a reference-frame qualification. Including an inertial (fictitious) force in the train frame, or using the ground’s inertial frame, explains the motion.')

en('l10-q2', 'The SI Base Units of Angular Momentum',
   'Angular momentum is used to describe gyroscopes. Its magnitude is L = rmv sinθ, where r is the distance to the rotation axis, m is the particle’s mass, v is its speed, and θ is the angle between r and v. Express angular momentum in SI base units.',
   ['kg·m²/s', 'kg·m/s', 'N·m/s', 'N·m·s'], 'A', [
   'Start from L = rmv sinθ. The factor sinθ is dimensionless, so it contributes no unit.',
   'The units of r, mass, and speed are m, kg, and m/s. Their product is kg·m²/s.',
   'N·m·s in D is equivalent to kg·m²/s, but the newton is a derived unit. Since the question asks for base units, choose A.'],
   '[L] = m × kg × (m/s) = kg·m²·s⁻¹',
   'An equivalent unit expression does not necessarily use base units only.')

en('l10-q3', 'Acceleration Just After a String Is Cut',
   'Two balls A and B, each of mass m, are connected by a light spring. A hangs from a string, and both balls are initially at rest. The string supporting A is cut. What are their instantaneous accelerations immediately afterward?',
   ['a_A = 2g, a_B = 0', 'a_A = a_B = g',
    'a_A = 0, a_B = 2g', 'a_A = a_B = g/2'], 'A; A accelerates vertically downward', [
   'Before the cut, B is in equilibrium, so the spring pulls B upward with force mg. It pulls A downward with an equal force mg.',
   'At the instant of cutting, the spring length has not changed, so its force remains mg. The tension in the upper string disappears immediately.',
   'A now experiences its weight mg and a downward spring force mg. The net force is 2mg downward, giving a_A = 2g downward.',
   'B still has equal and opposite weight and spring force. Its instantaneous net force is zero, so a_B = 0.'],
   'a_A = (mg + mg)/m = 2g downward; a_B = (mg − mg)/m = 0',
   'The spring force depends on deformation, which is unchanged at that instant. The balls do not immediately share free-fall acceleration.',
   'An upper string supports ball A. A vertical spring connects A to ball B below it.')

en('l10-q4', 'Motion After a Pulling Force Is Removed',
   'A block of mass m = 2 kg is initially at rest on a horizontal surface. A constant horizontal force F = 14 N pulls it to the right. The force is removed after the block travels 9 m. The coefficient of kinetic friction is μ = 0.5. Take g = 10 m/s². Find:\n(1) the acceleration magnitude a while the pulling force acts;\n(2) the speed v when the force is removed;\n(3) the additional distance x travelled after the force is removed.',
   [], '(1) 2 m/s²; (2) 6 m/s; (3) 3.6 m', [
   'Vertical equilibrium gives N = mg = 20 N. Kinetic friction is f = μmg = 0.5 × 2 × 10 = 10 N.',
   '(1) During the pull, F − f = ma. Thus a = (14 − 10)/2 = 2 m/s².',
   '(2) Starting from rest and moving 9 m: v² = 2as = 2 × 2 × 9 = 36. Therefore v = 6 m/s.',
   '(3) After the pull is removed, friction is unchanged and the deceleration magnitude is a₂ = f/m = 5 m/s². Using 0 − v² = −2a₂x gives x = 36/10 = 3.6 m. After the block stops, friction becomes zero; it does not reverse direction.'],
   'a₁ = (F − μmg)/m = 2 m/s²\nv = √(2a₁s) = 6 m/s\nx = v²/(2μg) = 3.6 m',
   'Removing the force changes the acceleration, while the velocity remains continuous at that instant.',
   'A block on a horizontal surface is pulled rightward by a constant force F.')

en('l10-q5', 'Two Stages: A Slope and a Level Track',
   'AB is a straight ski slope inclined at θ = 37°, joining a horizontal track BC smoothly at B. A sled of mass m = 15 kg, treated as a particle, starts from rest at A, accelerates uniformly down AB, and reaches B at 20 m/s. It then stops at C. The coefficient of kinetic friction is μ = 0.25 on both sections. Take g = 10 m/s², sin37° = 0.6, and cos37° = 0.8.\n(1) Find the length AB.\n(2) Find the total time from starting at A to stopping at C.',
   [], '(1) 50 m; (2) 13 s', [
   'Take downhill along AB as positive. The normal force is N₁ = mg cos37° and friction acts uphill. Newton’s second law gives a₁ = g(sin37° − μcos37°) = 10(0.6 − 0.25 × 0.8) = 4 m/s².',
   '(1) From v_B² = 2a₁s_AB, obtain s_AB = 20²/(2 × 4) = 50 m.',
   'The time on AB is t₁ = v_B/a₁ = 20/4 = 5 s.',
   'The sled enters BC at the same speed of 20 m/s. Its deceleration magnitude is a₂ = μg = 2.5 m/s², so t₂ = 20/2.5 = 8 s.',
   '(2) The total time is t = t₁ + t₂ = 5 + 8 = 13 s.'],
   'a_AB = 4 m/s²; AB = 50 m\na_BC = −2.5 m/s²; t_total = 5 + 8 = 13 s',
   'On the slope N = mg cosθ; on the horizontal N = mg. The friction forces are therefore different.',
   'A sled moves down inclined section AB, then continues along horizontal section BC until it stops.')

en('l11-q1', 'Apparent Weight in an Elevator',
   'The cartoons illustrate changes in apparent weight. Figure a represents an elevator at rest or moving at constant velocity. Which statement about the possible motions represented by figures b and c is correct?',
   ['Figure b may represent upward motion while slowing down.',
    'Figure b may represent upward motion while speeding up.',
    'Figure c may represent upward motion while speeding up.',
    'Figure c may represent downward motion while slowing down.'], 'B', [
   'Taking upward as positive gives N − mg = ma. If N > mg, apparent weight increases and acceleration is upward. If N < mg, apparent weight decreases and acceleration is downward.',
   'In b, the character is compressed, indicating a larger normal force and increased apparent weight. The elevator may be speeding up upward or slowing down downward. B is correct and A is incorrect.',
   'In c, the stretched or floating character indicates decreased apparent weight. Possible motions are speeding up downward or slowing down upward. Both C and D imply upward acceleration, so they are incorrect.'],
   'Increased apparent weight: N > mg, acceleration upward\nDecreased apparent weight: N < mg, acceleration downward',
   'Apparent weight depends on acceleration direction, not simply the direction of motion.',
   'Figure a (left): normal shape, at rest or constant velocity. Figure b (middle): compressed, increased apparent weight. Figure c (right): stretched or floating, decreased apparent weight.')

en('l11-q2', 'Reading a Squat-and-Stand Acceleration Graph',
   'The phyphox app uses a smartphone’s sensors for physics experiments. A student holds the phone horizontally, screen facing upward, and starts from a stationary standing position before squatting and standing up. The graph records vertical linear acceleration (z axis, upward positive). Take g = 9.8 m/s². Which statement is correct?',
   ['The velocity reverses direction during 0–2 s.',
    'The student completes two full squat-and-stand cycles during 0–4 s.',
    'The phone has decreased apparent weight throughout the squat and increased apparent weight throughout the rise.',
    'If the phone has mass 200 g, the upward force from the hand never exceeds 3.5 N during the motion.'], 'D', [
   'The graph shows linear acceleration, approximately zero at rest. During 0–2 s, its main pattern is negative followed by positive: the phone accelerates downward and then slows to rest while still moving downward. This is the squat. A change in acceleration sign does not imply a reversal of velocity. A is incorrect.',
   'During roughly 2–4 s, acceleration is positive followed by negative: the phone speeds up upward and then slows to rest, completing the rise. Thus 0–4 s contains one full squat-and-stand cycle. B is incorrect.',
   'The first half of the squat has decreased apparent weight and the second half increased apparent weight. The rise has the reverse sequence. C is incorrect.',
   'Using N = m(g + a), the maximum positive acceleration is about 6–7 m/s², below 7.7 m/s². Taking 7 m/s² as an approximate upper bound gives N_max ≲ 0.2(9.8 + 7) = 3.36 N < 3.5 N. D is correct.'],
   'v(t) = v₀ + ∫a dt; N = m(g + a)\nN ≤ 3.5 N ⇔ a ≤ 7.7 m/s² (m = 0.2 kg)',
   'Allow for measurement noise and use the main waveform and signed area. The sign of acceleration is not the sign of velocity.',
   'Vertical linear acceleration a (m/s²) versus time t (s), upward positive. From 0–2 s the main pulse is negative then positive; from 2–4 s it is positive then negative. The maximum is about 6–7 m/s².')

en('l11-q3', 'A Ball Falling onto a Spring',
   'A ball is released from rest at A and falls freely onto a light vertical spring standing on the ground. It starts compressing the spring at B, reaches its lowest point C, and then rebounds. Ignore air resistance. Which statement is correct?',
   ['Before reaching B, the ball falls freely with both increasing speed and increasing acceleration.',
    'The ball reaches its maximum speed between B and C.',
    'The ball has increased apparent weight throughout its downward motion from B to C.',
    'From A to C, the ball first has uniform acceleration and then uniform deceleration.'], 'B', [
   'Before B, the ball is in free fall. Its speed increases, but its acceleration is constant at g. A is incorrect.',
   'After contact, let x be the compression and take downward as positive. Then a = g − kx/m. Initially kx < mg, so the ball accelerates downward. At kx = mg, acceleration is zero and speed is maximum.',
   'Afterward kx > mg: acceleration is upward, but the ball is still moving downward and slows until its speed reaches zero at C. Thus the maximum-speed point lies between B and C. B is correct.',
   'From B to the maximum-speed point the spring force is less than weight, so apparent weight is reduced; afterward it is increased. C is incorrect. Since acceleration varies with compression, the motion after contact does not have constant acceleration or deceleration. D is incorrect.'],
   'a = g − kx/m; maximum speed ⇔ a = 0 ⇔ x = mg/k',
   'At the lowest point, velocity is zero but acceleration generally is not. Net force is zero at the maximum-speed point.',
   'The ball falls from A, contacts the spring at B, and compresses it until reaching the lowest point C.')

en('l11-q4', 'A String’s Breaking Limit and Maximum Acceleration',
   'Blocks A and B are connected by a light string on a smooth horizontal floor, with m_A = 2 kg and m_B = 4 kg. The maximum string tension is 8 N. Which applied force gives the greatest acceleration without breaking the string?',
   ['8 N, pulling B horizontally to the left.',
    '8 N, pulling A horizontally to the right.',
    '24 N, pulling B horizontally to the left.',
    '24 N, pulling A horizontally to the right.'], 'C', [
   'When B is pulled leftward, the string accelerates A. For A, T = m_Aa, so a ≤ 8/2 = 4 m/s².',
   'The total mass is 6 kg. The maximum applied force is F = (m_A + m_B)a = 6 × 4 = 24 N. This is choice C.',
   'When A is pulled rightward, the string accelerates B, so a ≤ 8/4 = 2 m/s². The maximum applied force in that direction is only 6 × 2 = 12 N.',
   'Pulling the heavier block B allows a greater system acceleration. If A were pulled rightward with 24 N, the tension would be T = 4 × (24/6) = 16 N, breaking the string.'],
   'Pull B: a_max = T_max/m_A = 4 m/s²; F_max = 24 N\nPull A: a_max = T_max/m_B = 2 m/s²; F_max = 12 N',
   'The applied force is not the string tension. Write a separate equation for the block accelerated by the string.',
   'On a smooth horizontal floor, B is on the left and A on the right, connected by a horizontal string.')

en('l11-q5', 'Four Blocks and a Force Sensor',
   'Four identical blocks, each of mass m, are arranged in a row on a horizontal floor. Each has coefficient of kinetic friction μ, and maximum static friction equals kinetic friction. A force sensor of negligible mass is fixed between blocks 1 and 2. At t = 0, a horizontal force F is applied to block 1, as shown. Which statements are correct?',
   ['If all four blocks are at rest, the contact forces from left to right have ratio 3:2:1.',
    'If all four blocks accelerate uniformly to the right together, the contact forces from left to right have ratio 3:2:1.',
    'If F increases linearly with time as F = kt, the sensor reads F₁ = μmg at t = μmg/k.',
    'If F increases linearly with time as F = kt, the blocks have acceleration 0.5μg at t = 6μmg/k.'], 'B and D', [
   'Let the contact forces be P₁₂, P₂₃, and P₃₄. At rest, each static friction force takes the value needed, up to μmg. The individual friction forces are unspecified, so the ratio 3:2:1 is not guaranteed. A is incorrect.',
   'When the blocks accelerate to the right together, each has kinetic friction μmg. Applying Newton’s second law to the rightmost three, two, and one blocks gives P₁₂ = 3m(a + μg), P₂₃ = 2m(a + μg), and P₃₄ = m(a + μg). Their ratio is 3:2:1. B is correct.',
   'At t = μmg/k, the applied force is μmg, below the total maximum static friction 4μmg, so the system has not begun sliding as a whole. The sensor reading depends on the static-friction distribution and need not be μmg. For example, friction on block 1 alone can balance F, leaving a zero sensor reading. C is incorrect.',
   'At t = 6μmg/k, F = 6μmg > 4μmg and the system is sliding. For all four blocks, F − 4μmg = 4ma. Hence a = (6μmg − 4μmg)/(4m) = 0.5μg. D is correct.'],
   'While sliding: a = F/(4m) − μg\nP₁₂ : P₂₃ : P₃₄ = 3 : 2 : 1\nF = 6μmg → a = 0.5μg',
   'Static friction need not equal μmg. Do not apply the sliding-state contact-force ratio automatically to a stationary system.',
   'Four equal blocks numbered 1–4 from left to right. Force F pushes block 1 rightward; the force sensor lies between blocks 1 and 2.')
