{
  "P Cycle": {
    "Physics": [
      {
        "term": "de Broglie Hypothesis",
        "category": "Quantum Mechanics",
        "definition": "Every moving particle has an associated wave. The wavelength of this matter wave is inversely proportional to the momentum of the particle.",
        "formula": "λ = h / mv  (λ = wavelength, h = Planck's constant, m = mass, v = velocity)",
        "example": "An electron moving at high speed has a very small wavelength, showing wave-like behaviour."
      },
      {
        "term": "Heisenberg's Uncertainty Principle",
        "category": "Quantum Mechanics",
        "definition": "It is impossible to simultaneously determine the exact position and exact momentum of a particle. The product of their uncertainties is always greater than or equal to h/4π.",
        "formula": "Δx · Δp ≥ h / 4π",
        "example": "If we know exactly where an electron is, we cannot know its speed at the same time."
      },
      {
        "term": "Wave Function (ψ)",
        "category": "Quantum Mechanics",
        "definition": "A mathematical function that describes the quantum state of a particle. Its square (|ψ|²) gives the probability of finding the particle at a given position.",
        "formula": "|ψ|² = probability density",
        "example": "Higher |ψ|² at a point means the electron is more likely to be found there."
      },
      {
        "term": "Schrödinger Wave Equation",
        "category": "Quantum Mechanics",
        "definition": "A fundamental equation of quantum mechanics that describes how the wave function of a quantum system changes over time.",
        "formula": "-(h²/8π²m) · d²ψ/dx² + Vψ = Eψ",
        "example": "Used to find energy levels of an electron in a hydrogen atom."
      },
      {
        "term": "Quantum Tunneling",
        "category": "Quantum Mechanics",
        "definition": "A quantum phenomenon where a particle passes through a potential energy barrier that it classically could not overcome. This is possible because of the wave nature of particles.",
        "example": "Tunneling is the basis for tunnel diodes and scanning tunneling microscopes."
      },
      {
        "term": "Fermi Energy",
        "category": "Electrical Properties",
        "definition": "The maximum energy that electrons in a metal occupy at absolute zero temperature (0 K). It is the highest filled energy level at 0 K.",
        "formula": "EF = (h²/8m)(3n/π)^(2/3)  where n = electron density",
        "example": "In copper, the Fermi energy is about 7 eV."
      },
      {
        "term": "Fermi-Dirac Statistics",
        "category": "Electrical Properties",
        "definition": "A statistical distribution that describes the probability of occupancy of energy states by electrons (fermions) at a given temperature.",
        "formula": "f(E) = 1 / (1 + e^((E-EF)/kT))",
        "example": "At T=0, all states below EF are full and all above are empty."
      },
      {
        "term": "Hall Effect",
        "category": "Electrical Properties",
        "definition": "When a current-carrying conductor is placed in a perpendicular magnetic field, a voltage (Hall voltage) develops perpendicular to both current and magnetic field.",
        "formula": "VH = RH · I · B / t  (RH = Hall coefficient)",
        "example": "Hall effect is used to determine whether a semiconductor is n-type or p-type."
      },
      {
        "term": "Superconductivity",
        "category": "Superconductivity",
        "definition": "The phenomenon where certain materials exhibit zero electrical resistance and expulsion of magnetic fields when cooled below a critical temperature (Tc).",
        "example": "Mercury becomes superconducting below 4.2 K."
      },
      {
        "term": "Meissner Effect",
        "category": "Superconductivity",
        "definition": "The expulsion of magnetic field lines from the interior of a superconductor when it transitions to the superconducting state. A superconductor is a perfect diamagnet.",
        "example": "A magnet floats above a superconductor due to the Meissner effect."
      },
      {
        "term": "Cooper Pairs",
        "category": "Superconductivity",
        "definition": "Pairs of electrons that are bound together via phonon interactions in a superconductor. These pairs have zero net spin and are responsible for superconductivity according to BCS theory.",
        "example": "In a superconductor, electrons pair up and flow without resistance."
      },
      {
        "term": "BCS Theory",
        "category": "Superconductivity",
        "definition": "Bardeen-Cooper-Schrieffer theory explains superconductivity as a result of Cooper pair formation via electron-phonon interaction, leading to a phase-coherent quantum state.",
        "example": "BCS theory successfully explains the energy gap in superconductors."
      },
      {
        "term": "Laser",
        "category": "Photonics",
        "definition": "Light Amplification by Stimulated Emission of Radiation. A device that emits highly monochromatic, coherent, and collimated light through stimulated emission.",
        "example": "Lasers are used in fiber optic communication, surgery, and barcode scanners."
      },
      {
        "term": "Stimulated Emission",
        "category": "Photonics",
        "definition": "A process where an incoming photon triggers an excited atom to emit a second photon with the same energy, phase, and direction as the incoming photon.",
        "example": "This is the core mechanism behind laser action."
      },
      {
        "term": "Optical Fiber",
        "category": "Photonics",
        "definition": "A thin glass or plastic fiber through which light propagates by total internal reflection, used for high-speed data transmission.",
        "formula": "NA = √(n₁² - n₂²)  (NA = Numerical Aperture)",
        "example": "Internet data travels thousands of kilometers via optical fiber cables."
      },
      {
        "term": "Numerical Aperture",
        "category": "Photonics",
        "definition": "A dimensionless number that characterizes the range of angles over which an optical fiber can accept light. It indicates the light-gathering ability of the fiber.",
        "formula": "NA = sin(θmax) = √(n₁² - n₂²)",
        "example": "A higher NA means the fiber can accept light over a wider angle."
      },
      {
        "term": "Qubit",
        "category": "Quantum Computing",
        "definition": "The fundamental unit of quantum information. Unlike a classical bit (0 or 1), a qubit can exist in a superposition of both 0 and 1 simultaneously.",
        "example": "A qubit is like a coin spinning in the air — it's both heads and tails until observed."
      },
      {
        "term": "Quantum Gate",
        "category": "Quantum Computing",
        "definition": "A basic quantum circuit element that manipulates qubits. Analogous to classical logic gates but reversible. Examples: Hadamard gate, CNOT gate, Pauli gates.",
        "example": "The Hadamard gate puts a qubit into equal superposition of |0⟩ and |1⟩."
      },
      {
        "term": "Superposition",
        "category": "Quantum Computing",
        "definition": "The ability of a quantum system to be in multiple states simultaneously until a measurement is made. This is what gives quantum computers their power.",
        "example": "A qubit in superposition can represent both 0 and 1 at the same time."
      },
      {
        "term": "Quantum Entanglement",
        "category": "Quantum Computing",
        "definition": "A phenomenon where two qubits become correlated so that the state of one instantly determines the state of the other, no matter the distance between them.",
        "example": "Bell states are the simplest examples of maximally entangled qubits."
      },
      {
        "term": "Total Internal Reflection",
        "category": "Photonics",
        "definition": "When light traveling from a denser medium hits the boundary at an angle greater than the critical angle, it is completely reflected back into the denser medium.",
        "formula": "θc = sin⁻¹(n₂/n₁)",
        "example": "Total internal reflection keeps light inside an optical fiber."
      }
    ],
    "Maths": [
      {
        "term": "Partial Derivative",
        "category": "Calculus",
        "definition": "The derivative of a function with respect to one variable while holding all other variables constant. Denoted as ∂f/∂x.",
        "formula": "∂f/∂x = lim(Δx→0) [f(x+Δx,y) - f(x,y)] / Δx",
        "example": "For f(x,y)=x²y, ∂f/∂x = 2xy and ∂f/∂y = x²."
      },
      {
        "term": "Jacobian",
        "category": "Calculus",
        "definition": "A matrix of all first-order partial derivatives of a vector-valued function. Its determinant (Jacobian determinant) is used in change of variable in multiple integrals.",
        "formula": "J = |∂(u,v)/∂(x,y)| = |∂u/∂x  ∂u/∂y; ∂v/∂x  ∂v/∂y|",
        "example": "Used when converting from Cartesian to polar coordinates in double integrals."
      },
      {
        "term": "Maxima and Minima",
        "category": "Calculus",
        "definition": "The highest (maximum) or lowest (minimum) values of a function in a given region. Found using the second derivative test for functions of two variables.",
        "formula": "Conditions: fx=0, fy=0; D = fxx·fyy - (fxy)² > 0 for extrema",
        "example": "Finding the minimum cost or maximum area in engineering optimization problems."
      },
      {
        "term": "Gradient (∇f)",
        "category": "Vector Calculus",
        "definition": "A vector that points in the direction of the greatest rate of increase of a scalar function. Its magnitude gives the rate of that increase.",
        "formula": "∇f = (∂f/∂x)i + (∂f/∂y)j + (∂f/∂z)k",
        "example": "The gradient of temperature tells you which direction temperature increases fastest."
      },
      {
        "term": "Divergence (∇·F)",
        "category": "Vector Calculus",
        "definition": "A scalar that measures how much a vector field spreads out or converges at a given point.",
        "formula": "∇·F = ∂Fx/∂x + ∂Fy/∂y + ∂Fz/∂z",
        "example": "Positive divergence means fluid is flowing outward (source); negative means inward (sink)."
      },
      {
        "term": "Curl (∇×F)",
        "category": "Vector Calculus",
        "definition": "A vector that measures the rotation or swirling tendency of a vector field at a point.",
        "formula": "∇×F = (∂Fz/∂y - ∂Fy/∂z)i - (∂Fz/∂x - ∂Fx/∂z)j + (∂Fy/∂x - ∂Fx/∂y)k",
        "example": "Curl of a magnetic field is related to the current density (Ampere's law)."
      },
      {
        "term": "Eigenvalue",
        "category": "Linear Algebra",
        "definition": "A scalar λ such that when a matrix A multiplies vector v, the result is just a scalar multiple of v. The fundamental equation is Av = λv.",
        "formula": "det(A - λI) = 0  (characteristic equation)",
        "example": "Eigenvalues of stress matrices are principal stresses in structural engineering."
      },
      {
        "term": "Eigenvector",
        "category": "Linear Algebra",
        "definition": "A non-zero vector that does not change its direction (only its magnitude) when a linear transformation is applied to it.",
        "formula": "Av = λv  →  (A - λI)v = 0",
        "example": "In PCA (machine learning), eigenvectors point in the directions of maximum variance."
      },
      {
        "term": "Rank of a Matrix",
        "category": "Linear Algebra",
        "definition": "The maximum number of linearly independent rows (or columns) in a matrix. It equals the number of non-zero rows in its echelon form.",
        "example": "A 3×3 matrix with rank 3 is invertible; with rank < 3 it is singular."
      },
      {
        "term": "Gauss Elimination",
        "category": "Numerical Methods",
        "definition": "A method to solve a system of linear equations by converting the augmented matrix to row echelon form using elementary row operations, then back-substituting.",
        "example": "Solving 3 equations with 3 unknowns by eliminating variables one at a time."
      },
      {
        "term": "Vector Space",
        "category": "Linear Algebra",
        "definition": "A collection of vectors that can be added together and multiplied by scalars, satisfying 8 axioms (closure, associativity, identity, inverse, distributivity, etc.).",
        "example": "The set of all 2D vectors (x,y) forms a vector space over real numbers."
      },
      {
        "term": "Linear Transformation",
        "category": "Linear Algebra",
        "definition": "A function T between two vector spaces that preserves vector addition and scalar multiplication: T(au+bv) = aT(u) + bT(v).",
        "formula": "T(u+v) = T(u)+T(v)  and  T(cu) = cT(u)",
        "example": "Rotation, scaling, and reflection are linear transformations in 2D."
      },
      {
        "term": "Rank-Nullity Theorem",
        "category": "Linear Algebra",
        "definition": "For a linear transformation T: V → W, the dimension of V equals the rank of T plus the nullity of T.",
        "formula": "dim(V) = rank(T) + nullity(T)",
        "example": "If T: R⁵ → R³ has rank 3, then its nullity is 2."
      },
      {
        "term": "Taylor Series (Two Variables)",
        "category": "Calculus",
        "definition": "An infinite series expansion of a function of two variables around a point (a,b) using partial derivatives.",
        "formula": "f(x,y) ≈ f(a,b) + fx·(x-a) + fy·(y-b) + (1/2!)[fxx(x-a)² + 2fxy(x-a)(y-b) + fyy(y-b)²] + ...",
        "example": "Used to approximate complex functions near a point in engineering analysis."
      }
    ],
    "EIT": [
      {
        "term": "Algorithm",
        "category": "Computing Fundamentals",
        "definition": "A finite, ordered set of well-defined instructions for solving a problem or accomplishing a task.",
        "example": "A recipe for making tea is an everyday algorithm: boil water → add tea bag → pour water → wait → remove bag."
      },
      {
        "term": "Binary System",
        "category": "Data Representation",
        "definition": "A number system using only two digits (0 and 1), which is the foundation of all digital computing. Each digit is called a bit.",
        "example": "The decimal number 5 is represented as 101 in binary."
      },
      {
        "term": "Operating System",
        "category": "Systems Software",
        "definition": "System software that manages computer hardware, software resources, and provides common services for computer programs. Acts as an interface between user and hardware.",
        "example": "Windows, Linux, macOS, and Android are all operating systems."
      },
      {
        "term": "RAM (Random Access Memory)",
        "category": "Data Storage",
        "definition": "Primary volatile memory where data currently being used by the CPU is stored. Data is lost when power is off.",
        "example": "When you open a program, it loads from hard disk into RAM for fast CPU access."
      },
      {
        "term": "Internet Protocol (IP)",
        "category": "Networking",
        "definition": "A set of rules governing the format of data sent over the internet. IP assigns addresses to devices so data can be routed correctly.",
        "example": "Every device on the internet has an IP address like 192.168.1.1."
      },
      {
        "term": "Cybersecurity",
        "category": "Security",
        "definition": "The practice of protecting computers, servers, mobile devices, electronic systems, networks, and data from malicious attacks, damage, or unauthorized access.",
        "example": "Using strong passwords and two-factor authentication are basic cybersecurity practices."
      },
      {
        "term": "Database",
        "category": "Software",
        "definition": "An organized collection of structured data, stored electronically in a computer system and managed by a Database Management System (DBMS).",
        "example": "A school database might store student names, roll numbers, marks, and attendance."
      },
      {
        "term": "SQL",
        "category": "Software",
        "definition": "Structured Query Language — a standard programming language for managing relational databases. Used for inserting, updating, deleting, and querying data.",
        "example": "SELECT * FROM students WHERE marks > 80; retrieves all students with marks above 80."
      },
      {
        "term": "HTML",
        "category": "Web Development",
        "definition": "HyperText Markup Language — the standard language for creating web pages. It uses tags to structure content like headings, paragraphs, images, and links.",
        "example": "<h1>Hello World</h1> creates a large heading on a webpage."
      },
      {
        "term": "CSS",
        "category": "Web Development",
        "definition": "Cascading Style Sheets — a language used to style HTML elements. Controls colors, fonts, spacing, and layout of web pages.",
        "example": "body { background-color: blue; } makes the webpage background blue."
      },
      {
        "term": "Cybersecurity — CIA Triad",
        "category": "Security",
        "definition": "The three core principles of information security: Confidentiality (only authorized access), Integrity (data is accurate and unaltered), Availability (systems are accessible when needed).",
        "example": "A hospital must ensure patient records are confidential, accurate, and always accessible."
      },
      {
        "term": "Phishing",
        "category": "Security",
        "definition": "A type of cyber attack where attackers trick users into revealing sensitive information (passwords, credit card numbers) by pretending to be a legitimate entity.",
        "example": "A fake email claiming to be from your bank asking you to click a link and enter your password."
      },
      {
        "term": "Encryption",
        "category": "Security",
        "definition": "The process of converting readable data (plaintext) into an unreadable format (ciphertext) using a key, so only authorized parties can decrypt and read it.",
        "example": "WhatsApp uses end-to-end encryption so only sender and receiver can read messages."
      },
      {
        "term": "Software Development Life Cycle (SDLC)",
        "category": "Software Engineering",
        "definition": "A structured process for planning, creating, testing, deploying, and maintaining software. Common models include Waterfall, Agile, and Spiral.",
        "example": "SDLC stages: Requirements → Design → Implementation → Testing → Deployment → Maintenance."
      }
    ],
    "ECE": [
      {
        "term": "Rectifier",
        "category": "Power Supplies",
        "definition": "An electronic circuit that converts alternating current (AC) into direct current (DC) using diodes.",
        "example": "A bridge rectifier uses 4 diodes and provides full-wave rectification."
      },
      {
        "term": "Amplifier",
        "category": "Analog Circuits",
        "definition": "An electronic circuit that increases the amplitude (voltage, current, or power) of a signal.",
        "formula": "Gain (A) = Output / Input  (in dB: A = 20·log(Vout/Vin))",
        "example": "A microphone amplifier boosts a weak voice signal to drive a speaker."
      },
      {
        "term": "Negative Feedback",
        "category": "Analog Circuits",
        "definition": "A technique where a portion of the output signal is fed back to the input in opposite phase, reducing gain but improving stability, bandwidth, and reducing distortion.",
        "example": "Op-amps commonly use negative feedback to set a precise, stable gain."
      },
      {
        "term": "Oscillator",
        "category": "Analog Circuits",
        "definition": "An electronic circuit that generates a continuous, repetitive waveform (sine, square, triangular) without any external input signal, using positive feedback.",
        "example": "A Wien Bridge oscillator generates a stable sine wave for audio frequency applications."
      },
      {
        "term": "Operational Amplifier (Op-Amp)",
        "category": "Analog Circuits",
        "definition": "A high-gain, direct-coupled differential amplifier with very high input impedance, very low output impedance, and very high open-loop gain.",
        "example": "Op-amps are used in comparators, adders, integrators, and differentiators."
      },
      {
        "term": "Amplitude Modulation (AM)",
        "category": "Communication",
        "definition": "A modulation technique where the amplitude of the carrier wave is varied in proportion to the message signal while the frequency remains constant.",
        "formula": "s(t) = [Ac + Am·cos(2πfmt)]·cos(2πfct)",
        "example": "AM radio broadcasts use amplitude modulation (e.g., AIR 1566 kHz)."
      },
      {
        "term": "Frequency Modulation (FM)",
        "category": "Communication",
        "definition": "A modulation technique where the frequency of the carrier wave is varied in proportion to the amplitude of the message signal while the amplitude remains constant.",
        "example": "FM radio (88–108 MHz) uses frequency modulation for high-quality audio broadcast."
      },
      {
        "term": "Microcontroller",
        "category": "Embedded Systems",
        "definition": "A compact integrated circuit designed to govern a specific operation in an embedded system. It contains a processor, memory (RAM, ROM), and I/O peripherals on a single chip.",
        "example": "Arduino uses an ATmega microcontroller to control LEDs, motors, and sensors."
      },
      {
        "term": "Boolean Algebra",
        "category": "Digital Logic",
        "definition": "A branch of algebra where values of variables are true or false (1 or 0). Uses operations AND, OR, and NOT to simplify and analyze digital circuits.",
        "example": "A·(A+B) = A is a Boolean identity used to simplify logic circuits."
      },
      {
        "term": "Logic Gate",
        "category": "Digital Logic",
        "definition": "A basic electronic component that performs a Boolean logic operation on one or more binary inputs to produce a single binary output.",
        "example": "AND gate: output is 1 only when all inputs are 1. OR gate: output is 1 when any input is 1."
      },
      {
        "term": "Full Adder",
        "category": "Digital Logic",
        "definition": "A combinational logic circuit that adds three binary bits (A, B, and carry-in) and produces a sum bit and a carry-out bit.",
        "formula": "Sum = A ⊕ B ⊕ Cin,  Carry = AB + BCin + ACin",
        "example": "Multiple full adders are cascaded to build an n-bit binary adder."
      },
      {
        "term": "ASK / FSK / PSK",
        "category": "Communication",
        "definition": "Digital modulation schemes: ASK varies amplitude, FSK varies frequency, PSK varies phase of the carrier to encode digital data (0s and 1s).",
        "example": "Wi-Fi uses QAM (advanced form of PSK+ASK) for high-speed data transmission."
      },
      {
        "term": "Bandwidth",
        "category": "Analog Circuits",
        "definition": "The range of frequencies over which a circuit operates effectively. It is the difference between the upper and lower cutoff frequencies.",
        "formula": "BW = f₂ - f₁  (f₁=lower cutoff, f₂=upper cutoff frequency)",
        "example": "An FM radio has a bandwidth of 200 kHz per channel."
      }
    ],
    "C Program": [
      {
        "term": "Variable",
        "category": "Language Basics",
        "definition": "A named memory location that stores a value which can be changed during program execution. It has a data type, name, and value.",
        "example": "int age = 20; declares an integer variable 'age' with value 20."
      },
      {
        "term": "Data Types in C",
        "category": "Language Basics",
        "definition": "Specifies the type of data a variable can hold: int (integers), float (decimals), char (characters), double (large decimals). Determines memory allocated.",
        "formula": "int: 4 bytes | float: 4 bytes | double: 8 bytes | char: 1 byte",
        "example": "float pi = 3.14159; stores the value of pi."
      },
      {
        "term": "If-Else Statement",
        "category": "Control Structures",
        "definition": "A decision-making statement that executes different code blocks based on whether a condition is true or false.",
        "example": "if (marks>=35) { printf('Pass'); } else { printf('Fail'); }"
      },
      {
        "term": "For Loop",
        "category": "Control Structures",
        "definition": "A loop that repeats a block of code a specific number of times. It has initialization, condition check, and increment/decrement in one line.",
        "example": "for(i=0; i<5; i++) { printf('%d', i); } prints 0 1 2 3 4."
      },
      {
        "term": "While Loop",
        "category": "Control Structures",
        "definition": "A loop that repeatedly executes a block as long as the given condition remains true. Checks condition before executing the body.",
        "example": "while(n>0) { printf('%d',n); n--; } counts down from n to 1."
      },
      {
        "term": "Array",
        "category": "Data Structures",
        "definition": "A collection of elements of the same data type stored in contiguous memory locations, accessed using an index starting from 0.",
        "example": "int marks[5] = {80,75,90,65,88}; stores 5 subject marks. Access: marks[0]=80."
      },
      {
        "term": "Pointer",
        "category": "Pointers",
        "definition": "A variable that stores the memory address of another variable. Allows direct memory access and manipulation.",
        "example": "int x=10; int *p = &x; *p gives 10, p gives the address of x."
      },
      {
        "term": "Function",
        "category": "Functions",
        "definition": "A self-contained block of code that performs a specific task. Functions promote code reusability and modularity.",
        "example": "int add(int a, int b) { return a+b; } is a function that returns the sum of two numbers."
      },
      {
        "term": "Recursion",
        "category": "Functions",
        "definition": "A programming technique where a function calls itself until it reaches a base case. Used for problems that can be broken into smaller sub-problems of the same type.",
        "example": "int factorial(int n) { if(n==1) return 1; return n*factorial(n-1); }"
      },
      {
        "term": "String",
        "category": "Arrays and Strings",
        "definition": "An array of characters terminated by a null character (\\0). In C, there is no built-in string type; strings are represented as character arrays.",
        "example": "char name[10] = 'Ravi'; stores the name. name[0]='R', name[4]='\\0'."
      },
      {
        "term": "Structure",
        "category": "User-Defined Types",
        "definition": "A user-defined data type that groups variables of different data types under a single name, used to represent a real-world entity.",
        "example": "struct Student { char name[20]; int roll; float marks; }; groups student details."
      },
      {
        "term": "Union",
        "category": "User-Defined Types",
        "definition": "A user-defined data type where all members share the same memory location. The size of a union is the size of its largest member.",
        "example": "Unlike struct, in union only one member can hold a value at a time to save memory."
      },
      {
        "term": "Scope of Variables",
        "category": "Language Basics",
        "definition": "The region of the program where a variable is accessible. Local variables exist only inside the function; global variables are accessible throughout the program.",
        "example": "A variable declared inside main() cannot be used inside another function."
      },
      {
        "term": "Dynamic Memory Allocation",
        "category": "Pointers",
        "definition": "Allocating memory at runtime using functions: malloc() allocates memory, calloc() allocates and initializes to zero, realloc() resizes, free() releases memory.",
        "example": "int *arr = (int*)malloc(n*sizeof(int)); allocates array of n integers at runtime."
      }
    ]
  },
  "C Cycle": {
    "AI": [
      {
        "term": "Artificial Intelligence (AI)",
        "category": "Introduction",
        "definition": "The simulation of human intelligence processes (learning, reasoning, problem-solving, perception) by computer systems. AI enables machines to perform tasks that normally require human intelligence.",
        "example": "Google Search, Alexa, self-driving cars, and ChatGPT are all AI applications."
      },
      {
        "term": "Machine Learning (ML)",
        "category": "Introduction",
        "definition": "A subset of AI where systems automatically learn and improve from experience (data) without being explicitly programmed. The system finds patterns in data.",
        "example": "Netflix recommends shows based on your watch history using ML algorithms."
      },
      {
        "term": "Deep Learning",
        "category": "Introduction",
        "definition": "A subset of machine learning using artificial neural networks with many layers (deep networks) to learn from large amounts of data. Especially powerful for images and speech.",
        "example": "Deep learning powers facial recognition on smartphones and real-time language translation."
      },
      {
        "term": "Neural Network",
        "category": "Machine Learning",
        "definition": "A computational model inspired by the human brain, consisting of interconnected nodes (neurons) organized in layers (input, hidden, output) that process information.",
        "example": "A neural network trained on handwritten digits can recognize any digit you write."
      },
      {
        "term": "Supervised Learning",
        "category": "Machine Learning",
        "definition": "A type of ML where the model is trained on labeled data (input-output pairs). The model learns to map inputs to correct outputs.",
        "example": "Training a model with photos labeled 'cat' or 'dog' so it can classify new photos."
      },
      {
        "term": "Unsupervised Learning",
        "category": "Machine Learning",
        "definition": "A type of ML where the model finds hidden patterns or structures in unlabeled data, without any guidance on what to look for.",
        "example": "Grouping customers into segments based on purchasing behavior without predefined categories."
      },
      {
        "term": "Regression",
        "category": "Machine Learning",
        "definition": "A supervised learning technique for predicting continuous numerical values based on input features. The simplest form is linear regression.",
        "formula": "y = mx + c  (simple linear regression: y=output, x=input, m=slope, c=intercept)",
        "example": "Predicting house prices based on area, location, and number of rooms."
      },
      {
        "term": "Classification",
        "category": "Machine Learning",
        "definition": "A supervised learning task where the output is a discrete class label. The model learns to assign inputs to one of several predefined categories.",
        "example": "Classifying emails as 'spam' or 'not spam'; diagnosing a disease as 'positive' or 'negative'."
      },
      {
        "term": "Clustering",
        "category": "Machine Learning",
        "definition": "An unsupervised learning technique that groups similar data points together into clusters based on their features, without predefined labels.",
        "example": "K-means clustering groups similar customer profiles for targeted marketing."
      },
      {
        "term": "Prompt Engineering",
        "category": "Generative AI",
        "definition": "The art and science of crafting effective inputs (prompts) to guide AI language models to produce desired, accurate, and relevant outputs.",
        "example": "Instead of 'explain AI', a good prompt is 'Explain AI to a 10-year-old using simple examples'."
      },
      {
        "term": "Zero-Shot Prompting",
        "category": "Generative AI",
        "definition": "Asking an AI model to perform a task without providing any examples. The model relies entirely on its training knowledge.",
        "example": "'Translate this sentence to French: I love engineering.' — no example translations given."
      },
      {
        "term": "Few-Shot Prompting",
        "category": "Generative AI",
        "definition": "Providing a few examples of the desired input-output format in the prompt to guide the AI model to understand the task pattern.",
        "example": "Giving 2-3 example Q&A pairs before asking the AI to answer a new question in the same style."
      },
      {
        "term": "Expert System",
        "category": "AI Applications",
        "definition": "An AI system that uses a knowledge base and inference engine to emulate the decision-making ability of a human expert in a specific domain.",
        "example": "MYCIN was an expert system that diagnosed bacterial infections and recommended antibiotics."
      },
      {
        "term": "Internet of Things (IoT)",
        "category": "AI Trends",
        "definition": "A network of physical devices embedded with sensors, software, and connectivity to collect and exchange data over the internet.",
        "example": "Smart home devices like Google Nest thermostat adjusting temperature automatically based on habits."
      },
      {
        "term": "Naïve Bayes Classifier",
        "category": "Machine Learning",
        "definition": "A probabilistic classifier based on Bayes' theorem that assumes all features are independent of each other. 'Naïve' because of this strong independence assumption.",
        "formula": "P(class|features) ∝ P(class) × Π P(featureᵢ|class)",
        "example": "Used in spam filters to classify emails based on word frequencies."
      },
      {
        "term": "Support Vector Machine (SVM)",
        "category": "Machine Learning",
        "definition": "A supervised learning algorithm that finds the optimal hyperplane that best separates data points of different classes with maximum margin.",
        "example": "SVM is used in image classification, bioinformatics, and text classification."
      }
    ],
    "Chemistry": [
      {
        "term": "Organic Semiconductor",
        "category": "Functional Materials",
        "definition": "Carbon-based materials that exhibit semiconductor properties. Used in organic electronic devices like OLEDs and organic transistors. Includes p-type (pentacene) and n-type (perfluoropentacene).",
        "example": "Pentacene is a p-type organic semiconductor used in thin-film transistors."
      },
      {
        "term": "Quantum Dot",
        "category": "Quantum Materials",
        "definition": "A semiconductor nanocrystal (1–10 nm) whose electronic properties change dramatically with size due to quantum confinement effects. They emit different colors of light based on size.",
        "example": "Larger quantum dots emit red light; smaller ones emit blue light — used in QLED TVs."
      },
      {
        "term": "Quantum Confinement Effect",
        "category": "Quantum Materials",
        "definition": "When the size of a semiconductor particle is reduced to the nanoscale, its electronic energy levels become discrete (quantized), causing size-dependent optical and electrical properties.",
        "example": "CdSe quantum dots of 2 nm emit blue light while 6 nm dots emit red light."
      },
      {
        "term": "OLED (Organic Light Emitting Diode)",
        "category": "Display Systems",
        "definition": "A type of display technology where an organic compound emits light in response to an electric current. OLEDs produce their own light (no backlight needed), offering better contrast.",
        "example": "Smartphone AMOLED screens use OLEDs for vivid colors and true black display."
      },
      {
        "term": "Conducting Polymer",
        "category": "Polymers",
        "definition": "A polymer that can conduct electricity. Unlike most plastics (insulators), conducting polymers have alternating single and double bonds (conjugated system) allowing electron flow.",
        "example": "Polyaniline is a conducting polymer used in sensors, batteries, and corrosion protection."
      },
      {
        "term": "Li-Ion Battery",
        "category": "Energy Systems",
        "definition": "A rechargeable battery where lithium ions move from negative to positive electrode during discharge, and back during charging. High energy density, lightweight, no memory effect.",
        "example": "Smartphones, laptops, and electric vehicles use lithium-ion batteries."
      },
      {
        "term": "Fuel Cell",
        "category": "Energy Systems",
        "definition": "An electrochemical device that converts chemical energy from a fuel (usually hydrogen) directly into electricity through an oxidation reaction, with water as the only by-product.",
        "example": "Hydrogen fuel cells power some buses and the NASA space shuttles."
      },
      {
        "term": "Corrosion",
        "category": "Corrosion Science",
        "definition": "The gradual destruction of a material (usually metal) by chemical or electrochemical reaction with its environment. Rust forming on iron is the most common example.",
        "example": "Iron + Water + Oxygen → Fe₂O₃·xH₂O (rust). Costs industries billions per year."
      },
      {
        "term": "Galvanization",
        "category": "Corrosion Control",
        "definition": "The process of applying a protective zinc coating to steel or iron to prevent rusting. Zinc acts as a sacrificial anode — it corrodes before the iron does.",
        "example": "Steel pipes, traffic barriers, and metal roofing sheets are galvanized."
      },
      {
        "term": "Green Chemistry",
        "category": "Green Materials",
        "definition": "The design of chemical products and processes that reduce or eliminate the use and generation of hazardous substances. Follows 12 principles of green chemistry.",
        "example": "Using water as solvent instead of toxic organic solvents is a green chemistry approach."
      },
      {
        "term": "Biosensor",
        "category": "Sensors",
        "definition": "An analytical device that combines a biological recognition element (enzyme, antibody) with a transducer to detect and quantify a specific biological or chemical substance.",
        "formula": "Glucose + O₂ → Gluconic acid + H₂O₂  (detected electrochemically)",
        "example": "Blood glucose meters used by diabetic patients are biosensors."
      },
      {
        "term": "E-Waste",
        "category": "E-Waste Management",
        "definition": "Electronic waste — discarded electrical and electronic equipment. Contains both valuable materials (gold, silver, copper) and hazardous substances (lead, mercury, cadmium).",
        "example": "Old mobile phones, computers, and televisions are common sources of e-waste."
      },
      {
        "term": "Nernst Equation",
        "category": "Energy Systems",
        "definition": "Relates the electrode potential of a cell to the standard potential and the concentrations of the ions involved in the electrochemical reaction.",
        "formula": "E = E° - (RT/nF)·ln(Q)  or  E = E° - (0.0591/n)·log(Q) at 25°C",
        "example": "Used to calculate the EMF of a concentration cell at non-standard conditions."
      },
      {
        "term": "Polylactic Acid (PLA)",
        "category": "Biomaterials",
        "definition": "A biodegradable thermoplastic derived from renewable resources (corn starch, sugarcane). Widely used in 3D printing and biodegradable packaging.",
        "example": "PLA filament is the most popular material for desktop 3D printers."
      },
      {
        "term": "Sol-Gel Method",
        "category": "Nanomaterials",
        "definition": "A wet chemical technique for synthesizing nanomaterials by converting a liquid 'sol' into a solid 'gel' network, then drying. Produces high-purity, homogeneous nanomaterials.",
        "example": "TiO₂ nanomaterials for ReRAM memory devices are synthesized by the sol-gel method."
      }
    ],
    "Maths": [
      {
        "term": "Bisection Method",
        "category": "Numerical Methods",
        "definition": "A root-finding method that repeatedly halves an interval [a,b] where a function changes sign, converging to the root. Simple but slow convergence.",
        "formula": "xmid = (a+b)/2; replace a or b with xmid based on sign of f(xmid)",
        "example": "Finding the root of x³ - x - 2 = 0 between x=1 and x=2."
      },
      {
        "term": "Newton-Raphson Method",
        "category": "Numerical Methods",
        "definition": "A fast iterative root-finding method that uses the tangent line at a current approximation to find the next better approximation.",
        "formula": "x(n+1) = x(n) - f(x(n)) / f'(x(n))",
        "example": "Converges in very few iterations for well-behaved functions; fast but requires derivative."
      },
      {
        "term": "Gauss-Seidel Method",
        "category": "Numerical Methods",
        "definition": "An iterative method for solving a system of linear equations. Each variable is updated using the most recently computed values of the other variables.",
        "example": "Faster convergence than Gauss-Jacobi method because it uses updated values immediately."
      },
      {
        "term": "Lagrange Interpolation",
        "category": "Interpolation",
        "definition": "A method of finding a polynomial that passes through a given set of data points. Does not require equally spaced points.",
        "formula": "P(x) = Σ [yᵢ · Πⱼ≠ᵢ (x-xⱼ)/(xᵢ-xⱼ)]",
        "example": "Given data points of temperature vs time, find temperature at any intermediate time."
      },
      {
        "term": "Simpson's 1/3 Rule",
        "category": "Numerical Integration",
        "definition": "A numerical integration method that approximates the integral of a function by fitting parabolas over pairs of subintervals.",
        "formula": "∫f(x)dx ≈ (h/3)[f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + f(xₙ)]",
        "example": "Used to numerically integrate functions that cannot be integrated analytically."
      },
      {
        "term": "Runge-Kutta 4th Order (RK4)",
        "category": "Numerical Methods",
        "definition": "A widely used method for solving ordinary differential equations numerically. It uses four slope estimates to give highly accurate results.",
        "formula": "y(n+1) = yn + (h/6)(k₁ + 2k₂ + 2k₃ + k₄)",
        "example": "Used to simulate physical systems like projectile motion and circuit transients."
      },
      {
        "term": "Trapezoidal Rule",
        "category": "Numerical Integration",
        "definition": "Approximates the area under a curve by dividing it into trapezoids. Simple but less accurate than Simpson's rule.",
        "formula": "∫f(x)dx ≈ (h/2)[f(x₀) + 2f(x₁) + 2f(x₂) + ... + f(xₙ)]",
        "example": "Used when data points are available at equal intervals and a quick estimate is needed."
      },
      {
        "term": "Truncation Error",
        "category": "Error Analysis",
        "definition": "The error introduced when an infinite mathematical process (like a Taylor series) is approximated by a finite number of terms.",
        "example": "Using only 3 terms of e^x = 1 + x + x²/2! + ... introduces truncation error."
      },
      {
        "term": "Bernoulli's Differential Equation",
        "category": "Differential Equations",
        "definition": "A nonlinear first-order ODE of the form dy/dx + P(x)y = Q(x)yⁿ. Solved by substituting v = y^(1-n) to convert it to a linear equation.",
        "formula": "dy/dx + P(x)y = Q(x)yⁿ → substitute v = y^(1-n)",
        "example": "Models population growth with limiting resources."
      },
      {
        "term": "Euler's Method",
        "category": "Numerical Methods",
        "definition": "The simplest numerical method for solving ODEs. Uses the tangent line at a point to step forward to the next approximate solution value.",
        "formula": "y(n+1) = yn + h·f(xn, yn)",
        "example": "Simple and intuitive, but requires small step size h for accuracy."
      }
    ],
    "EEE": [
      {
        "term": "Ohm's Law",
        "category": "DC Circuits",
        "definition": "The voltage across a conductor is directly proportional to the current flowing through it, provided temperature remains constant.",
        "formula": "V = I × R  (Voltage = Current × Resistance)",
        "example": "A 12Ω resistor with 2A flowing through it has 24V across it."
      },
      {
        "term": "Kirchhoff's Current Law (KCL)",
        "category": "DC Circuits",
        "definition": "The total current entering a node (junction) equals the total current leaving it. Based on conservation of electric charge.",
        "formula": "ΣI(entering) = ΣI(leaving)  OR  ΣI = 0 at a node",
        "example": "If 3A and 2A enter a node, then 5A must leave it through other branches."
      },
      {
        "term": "Kirchhoff's Voltage Law (KVL)",
        "category": "DC Circuits",
        "definition": "The algebraic sum of all voltages around any closed loop in a circuit is zero. Based on conservation of energy.",
        "formula": "ΣV = 0 around any closed loop",
        "example": "In a loop with a 12V battery and two resistors (4V drop and 8V drop): 12-4-8=0."
      },
      {
        "term": "RMS Value",
        "category": "AC Circuits",
        "definition": "Root Mean Square value — the equivalent DC value that produces the same heating effect as the AC signal. For a sinusoidal wave, it is 1/√2 times the peak value.",
        "formula": "Vrms = Vpeak / √2 = 0.707 × Vpeak",
        "example": "Indian household supply is 230V RMS (peak is about 325V)."
      },
      {
        "term": "Power Factor",
        "category": "AC Circuits",
        "definition": "The ratio of real power (W) to apparent power (VA) in an AC circuit. It indicates how efficiently power is being used. PF = 1 for purely resistive loads.",
        "formula": "PF = cos(φ) = P/S  where φ = phase angle between V and I",
        "example": "An induction motor with PF=0.8 means only 80% of apparent power does useful work."
      },
      {
        "term": "DC Generator",
        "category": "DC Machines",
        "definition": "A machine that converts mechanical energy into DC electrical energy based on Faraday's law of electromagnetic induction. Uses commutator to convert AC to DC.",
        "formula": "E = (φZNP) / (60A)  (induced EMF equation)",
        "example": "Generators at power stations convert turbine rotation into electrical energy."
      },
      {
        "term": "DC Motor",
        "category": "DC Machines",
        "definition": "A machine that converts DC electrical energy into mechanical (rotational) energy. Based on the force experienced by a current-carrying conductor in a magnetic field.",
        "formula": "Back EMF: Eb = V - IaRa;  Torque: T ∝ φIa",
        "example": "DC motors are used in electric vehicles, elevators, and industrial machinery."
      },
      {
        "term": "Transformer",
        "category": "AC Machines",
        "definition": "A static device that transfers electrical energy between circuits through electromagnetic induction, changing voltage and current levels while keeping frequency constant.",
        "formula": "V₁/V₂ = N₁/N₂ = I₂/I₁  (turns ratio)",
        "example": "Step-up transformers increase voltage from 11kV to 220kV for long-distance transmission."
      },
      {
        "term": "Induction Motor",
        "category": "AC Machines",
        "definition": "An AC motor where the rotor current is induced by the rotating magnetic field of the stator. Most widely used industrial motor. No electrical connection to rotor needed.",
        "formula": "Slip: s = (Ns - N) / Ns  where Ns=synchronous speed, N=rotor speed",
        "example": "Fans, pumps, compressors, and most industrial machinery use induction motors."
      },
      {
        "term": "MCB (Miniature Circuit Breaker)",
        "category": "Safety",
        "definition": "An electromechanical device that automatically interrupts electrical flow when it detects overload or short circuit. Reusable — can be reset after tripping.",
        "example": "MCBs in home distribution boards protect wiring from damage due to excess current."
      },
      {
        "term": "Earthing",
        "category": "Safety",
        "definition": "Connecting the metallic parts of electrical equipment to the earth (ground) to prevent electric shock. In case of a fault, current flows safely to earth.",
        "example": "Plate earthing: a copper plate buried 3m deep provides a safe path for fault current."
      },
      {
        "term": "Three-Phase System",
        "category": "AC Circuits",
        "definition": "A power supply system with three alternating currents of the same frequency and amplitude, each displaced by 120° from each other. More efficient than single phase.",
        "formula": "Star: VL = √3·Vph; Delta: IL = √3·Iph",
        "example": "Industrial machinery and large appliances use three-phase power for efficiency."
      },
      {
        "term": "Slip (Induction Motor)",
        "category": "AC Machines",
        "definition": "The difference between the synchronous speed (of the rotating magnetic field) and the actual rotor speed, expressed as a fraction of synchronous speed.",
        "formula": "s = (Ns - N) / Ns × 100%  (typical value: 2–8%)",
        "example": "If Ns=1500 rpm and N=1450 rpm, slip = (1500-1450)/1500 = 3.33%."
      }
    ],
    "Python": [
      {
        "term": "Variable (Python)",
        "category": "Basics",
        "definition": "A name that refers to a value stored in memory. Python variables are dynamically typed — no need to declare the type; it is inferred from the assigned value.",
        "example": "name = 'Ravi'  →  Python knows it's a string. age = 20  →  Python knows it's an integer."
      },
      {
        "term": "List",
        "category": "Data Structures",
        "definition": "An ordered, mutable (changeable) collection of items in Python. Can hold items of different data types. Created with square brackets [].",
        "example": "marks = [85, 90, 78, 92]  →  marks[0] gives 85. marks.append(88) adds 88 to the list."
      },
      {
        "term": "Tuple",
        "category": "Data Structures",
        "definition": "An ordered, immutable (unchangeable) collection of items in Python. Once created, its elements cannot be modified. Created with parentheses ().",
        "example": "coordinates = (10, 20)  →  coordinates[0] gives 10. Cannot do coordinates[0] = 5."
      },
      {
        "term": "Dictionary",
        "category": "Data Structures",
        "definition": "An unordered, mutable collection of key-value pairs in Python. Keys are unique. Created with curly braces {}.",
        "example": "student = {'name':'Ravi', 'marks':90}  →  student['name'] gives 'Ravi'."
      },
      {
        "term": "Function (Python)",
        "category": "Functions",
        "definition": "A block of reusable code defined with the 'def' keyword. Functions can take parameters and return values.",
        "example": "def greet(name):  return 'Hello, ' + name  →  greet('Ravi') returns 'Hello, Ravi'."
      },
      {
        "term": "Class and Object",
        "category": "OOP",
        "definition": "A class is a blueprint for creating objects (instances). It defines attributes (data) and methods (functions). An object is a specific instance of a class.",
        "example": "class Dog:  def bark(self): print('Woof!')  →  d = Dog();  d.bark() prints 'Woof!'."
      },
      {
        "term": "Inheritance",
        "category": "OOP",
        "definition": "A mechanism where a child class derives attributes and methods from a parent class. Promotes code reuse and hierarchical organization.",
        "example": "class Animal:  def eat(self): pass  →  class Dog(Animal):  inherits eat() from Animal."
      },
      {
        "term": "Exception Handling",
        "category": "Error Handling",
        "definition": "A mechanism to handle runtime errors gracefully using try-except blocks, preventing the program from crashing.",
        "example": "try: x=10/0  except ZeroDivisionError: print('Cannot divide by zero')  → handles the error."
      },
      {
        "term": "NumPy Array",
        "category": "Libraries",
        "definition": "A powerful N-dimensional array object from the NumPy library. Supports mathematical operations on entire arrays at once (vectorization), much faster than Python lists.",
        "example": "import numpy as np; arr = np.array([1,2,3]); arr*2 gives array([2,4,6])."
      },
      {
        "term": "File Handling",
        "category": "Files",
        "definition": "Reading from and writing to files in Python using the open() function. Files can be opened in read ('r'), write ('w'), or append ('a') modes.",
        "example": "f = open('data.txt','r'); content = f.read(); f.close()  →  reads a file."
      },
      {
        "term": "Lambda Function",
        "category": "Functions",
        "definition": "A small, anonymous (unnamed) function defined in one line using the 'lambda' keyword. Used for short, throwaway functions.",
        "example": "square = lambda x: x**2  →  square(5) returns 25."
      },
      {
        "term": "List Comprehension",
        "category": "Data Structures",
        "definition": "A concise way to create lists in Python using a single line of code combining a for loop and optional condition.",
        "example": "squares = [x**2 for x in range(5)]  →  gives [0, 1, 4, 9, 16]."
      },
      {
        "term": "Polymorphism",
        "category": "OOP",
        "definition": "The ability of different classes to be treated as instances of the same class through a common interface. Same function name behaves differently for different classes.",
        "example": "def area(shape): shape.compute_area()  →  works for Circle, Square, Triangle differently."
      },
      {
        "term": "Module",
        "category": "Libraries",
        "definition": "A Python file containing Python code (functions, classes, variables) that can be imported and used in other Python programs.",
        "example": "import math; math.sqrt(16) returns 4.0. The 'math' module provides mathematical functions."
      }
    ]
  }
}
