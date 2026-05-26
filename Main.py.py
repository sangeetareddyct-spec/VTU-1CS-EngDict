import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import random

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")
FAV_FILE  = os.path.join(os.path.dirname(__file__), "favorites.json")

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_favs():
    if os.path.exists(FAV_FILE):
        with open(FAV_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_favs(favs):
    with open(FAV_FILE, "w", encoding="utf-8") as f:
        json.dump(favs, f, indent=2)

CYCLE_COLORS = {
    "P Cycle": "#3B82F6",
    "C Cycle": "#8B5CF6"
}

SUBJECT_ICONS = {
    "Physics":      "⚛",
    "Maths":        "∑",
    "EIT":          "💻",
    "ECE":          "📡",
    "C Program":    "©",
    "AI":           "🤖",
    "Chemistry":    "🧪",
    "EEE":          "⚡",
    "Python":       "🐍",
}

class EnggDictApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VTU Engineering Dictionary — 1st Year CS")
        self.geometry("1100x720")
        self.configure(bg="#F8F9FA")
        self.resizable(True, True)

        self.all_data   = load_data()
        self.favs       = load_favs()
        self.cur_subject = None
        self.cur_cycle   = None
        self.search_var  = tk.StringVar()
        self.search_var.trace("w", lambda *a: self.do_search())
        self.quiz_score  = [0, 0]  # correct, total

        self._build_ui()
        self.show_home()

    # ── UI skeleton ──────────────────────────────────────────────────────────

    def _build_ui(self):
        # ── top bar
        top = tk.Frame(self, bg="#1E293B", pady=10)
        top.pack(fill="x")
        tk.Label(top, text="📚 VTU Engineering Dictionary",
                 bg="#1E293B", fg="white",
                 font=("Segoe UI", 16, "bold")).pack(side="left", padx=16)

        self.search_entry = tk.Entry(top, textvariable=self.search_var,
                                     font=("Segoe UI", 12),
                                     width=30, relief="flat",
                                     bg="#334155", fg="white",
                                     insertbackground="white")
        self.search_entry.pack(side="left", padx=8, ipady=4)
        tk.Label(top, text="🔍", bg="#1E293B", fg="#94A3B8",
                 font=("Segoe UI", 14)).pack(side="left")

        nav_btns = [("🏠 Home","show_home"),
                    ("⭐ Favorites","show_favs"),
                    ("🧠 Quiz","show_quiz")]
        for label, cmd in nav_btns:
            tk.Button(top, text=label, command=getattr(self, cmd),
                      bg="#334155", fg="white",
                      font=("Segoe UI", 10), relief="flat",
                      padx=12, pady=4,
                      activebackground="#475569",
                      activeforeground="white",
                      cursor="hand2").pack(side="right", padx=4)

        # ── main area (sidebar + content)
        main = tk.Frame(self, bg="#F8F9FA")
        main.pack(fill="both", expand=True)

        # sidebar
        self.sidebar = tk.Frame(main, bg="#1E293B", width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="CYCLES", bg="#1E293B",
                 fg="#64748B", font=("Segoe UI", 9, "bold")).pack(pady=(16,4), padx=12, anchor="w")

        self.sidebar_inner = tk.Frame(self.sidebar, bg="#1E293B")
        self.sidebar_inner.pack(fill="both", expand=True, padx=8)

        # content area
        content_wrap = tk.Frame(main, bg="#F8F9FA")
        content_wrap.pack(side="left", fill="both", expand=True)

        self.canvas = tk.Canvas(content_wrap, bg="#F8F9FA", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(content_wrap, orient="vertical",
                                       command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.bind("<Configure>",
                         lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>",
                             lambda e: self.canvas.yview_scroll(-1*(e.delta//120), "units"))

        self.content = tk.Frame(self.canvas, bg="#F8F9FA")
        self.canvas.create_window((0,0), window=self.content, anchor="nw")
        self.content.bind("<Configure>",
                          lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self._build_sidebar()

    def _build_sidebar(self):
        for w in self.sidebar_inner.winfo_children():
            w.destroy()

        cycles = {"P Cycle": ["Physics","Maths","EIT","ECE","C Program"],
                  "C Cycle": ["AI","Chemistry","Maths","EEE","Python"]}

        for cycle, subjects in cycles.items():
            color = CYCLE_COLORS[cycle]
            cyc_btn = tk.Button(self.sidebar_inner,
                                text=f"● {cycle}",
                                bg="#1E293B", fg=color,
                                font=("Segoe UI", 10, "bold"),
                                relief="flat", anchor="w",
                                pady=6, padx=4,
                                activebackground="#0F172A",
                                activeforeground=color,
                                cursor="hand2",
                                command=lambda c=cycle: self.show_cycle(c))
            cyc_btn.pack(fill="x", pady=2)

            for subj in subjects:
                icon = SUBJECT_ICONS.get(subj, "•")
                s_btn = tk.Button(self.sidebar_inner,
                                  text=f"  {icon} {subj}",
                                  bg="#1E293B", fg="#CBD5E1",
                                  font=("Segoe UI", 9),
                                  relief="flat", anchor="w",
                                  pady=4, padx=8,
                                  activebackground="#0F172A",
                                  activeforeground="white",
                                  cursor="hand2",
                                  command=lambda c=cycle,s=subj: self.show_subject(c,s))
                s_btn.pack(fill="x")

    # ── page builders ─────────────────────────────────────────────────────────

    def _clear(self):
        for w in self.content.winfo_children():
            w.destroy()
        self.canvas.yview_moveto(0)

    def show_home(self):
        self._clear()
        self.search_var.set("")

        tk.Label(self.content, text="Welcome to VTU Engineering Dictionary!",
                 bg="#F8F9FA", fg="#1E293B",
                 font=("Segoe UI", 18, "bold")).pack(pady=(30,4), padx=20)
        tk.Label(self.content,
                 text="1st Year CS Stream  •  P Cycle & C Cycle  •  All Subjects",
                 bg="#F8F9FA", fg="#64748B",
                 font=("Segoe UI", 11)).pack(pady=(0,20))

        # stats row
        stats_frame = tk.Frame(self.content, bg="#F8F9FA")
        stats_frame.pack(pady=10)
        total_terms = sum(len(v) for s in self.all_data.values() for v in s.values())
        total_subj  = sum(len(v) for v in self.all_data.values())
        for label, val in [("📚 Total Terms", total_terms),
                           ("📖 Subjects", total_subj),
                           ("⭐ Favorites", len(self.favs))]:
            card = tk.Frame(stats_frame, bg="white",
                            relief="solid", bd=1)
            card.pack(side="left", padx=10, ipadx=20, ipady=10)
            tk.Label(card, text=str(val), bg="white", fg="#3B82F6",
                     font=("Segoe UI", 22, "bold")).pack()
            tk.Label(card, text=label, bg="white", fg="#64748B",
                     font=("Segoe UI", 10)).pack()

        # cycle cards
        tk.Label(self.content, text="Select a Cycle",
                 bg="#F8F9FA", fg="#1E293B",
                 font=("Segoe UI", 13, "bold")).pack(pady=(20,8))

        cycles_frame = tk.Frame(self.content, bg="#F8F9FA")
        cycles_frame.pack()

        cycle_info = {
            "P Cycle": ("📘","Physics · Maths · EIT · ECE · C Program",
                        "#DBEAFE","#1D4ED8"),
            "C Cycle": ("📗","AI · Chemistry · Maths · EEE · Python",
                        "#EDE9FE","#6D28D9"),
        }
        for cycle, (icon,subs,bg,fg) in cycle_info.items():
            card = tk.Frame(cycles_frame, bg=bg, relief="solid", bd=1)
            card.pack(side="left", padx=16, pady=8, ipadx=20, ipady=14)
            tk.Label(card, text=f"{icon}  {cycle}", bg=bg, fg=fg,
                     font=("Segoe UI", 14, "bold")).pack()
            tk.Label(card, text=subs, bg=bg, fg="#475569",
                     font=("Segoe UI", 9)).pack(pady=(4,8))
            tk.Button(card, text="Open →", bg=fg, fg="white",
                      font=("Segoe UI", 10), relief="flat",
                      padx=14, pady=4, cursor="hand2",
                      activebackground=fg,
                      command=lambda c=cycle: self.show_cycle(c)).pack()

        # Quick tip
        tk.Label(self.content,
                 text="💡 Tip: Use the search bar above to instantly find any term!",
                 bg="#FEF3C7", fg="#92400E",
                 font=("Segoe UI", 10), relief="solid", bd=1,
                 padx=16, pady=8).pack(pady=20)

    def show_cycle(self, cycle):
        self._clear()
        self.cur_cycle = cycle
        color = CYCLE_COLORS[cycle]

        tk.Label(self.content, text=f"● {cycle}",
                 bg="#F8F9FA", fg=color,
                 font=("Segoe UI", 16, "bold")).pack(pady=(20,4), padx=20, anchor="w")
        tk.Label(self.content, text="Choose a subject to explore",
                 bg="#F8F9FA", fg="#64748B",
                 font=("Segoe UI", 11)).pack(padx=20, anchor="w", pady=(0,12))

        subjects = list(self.all_data.get(cycle, {}).keys())
        grid = tk.Frame(self.content, bg="#F8F9FA")
        grid.pack(padx=20, pady=8)

        for i, subj in enumerate(subjects):
            icon = SUBJECT_ICONS.get(subj, "📖")
            count = len(self.all_data[cycle].get(subj, []))
            card = tk.Frame(grid, bg="white", relief="solid", bd=1, cursor="hand2")
            card.grid(row=i//3, column=i%3, padx=10, pady=10, ipadx=18, ipady=14, sticky="nsew")
            tk.Label(card, text=icon, bg="white",
                     font=("Segoe UI", 28)).pack()
            tk.Label(card, text=subj, bg="white", fg="#1E293B",
                     font=("Segoe UI", 12, "bold")).pack()
            tk.Label(card, text=f"{count} terms", bg="white", fg="#64748B",
                     font=("Segoe UI", 9)).pack(pady=(2,6))
            tk.Button(card, text="Explore →", bg=color, fg="white",
                      font=("Segoe UI", 9), relief="flat",
                      padx=10, pady=3, cursor="hand2",
                      activebackground=color,
                      command=lambda c=cycle,s=subj: self.show_subject(c,s)).pack()

    def show_subject(self, cycle, subject):
        self._clear()
        self.cur_cycle   = cycle
        self.cur_subject = subject
        color = CYCLE_COLORS[cycle]
        terms = self.all_data.get(cycle, {}).get(subject, [])

        # header
        hdr = tk.Frame(self.content, bg=color)
        hdr.pack(fill="x")
        icon = SUBJECT_ICONS.get(subject, "📖")
        tk.Label(hdr, text=f"{icon}  {subject}",
                 bg=color, fg="white",
                 font=("Segoe UI", 16, "bold"),
                 padx=16, pady=12).pack(side="left")
        tk.Label(hdr, text=f"{cycle}  •  {len(terms)} terms",
                 bg=color, fg="#BFDBFE",
                 font=("Segoe UI", 10)).pack(side="right", padx=16)

        # terms
        for item in terms:
            self._term_card(self.content, item, cycle, subject)

    def _term_card(self, parent, item, cycle, subject):
        card = tk.Frame(parent, bg="white", relief="solid", bd=1)
        card.pack(fill="x", padx=16, pady=6)

        # header row
        hdr = tk.Frame(card, bg="white")
        hdr.pack(fill="x", padx=12, pady=(10,4))

        is_fav = item["term"] in self.favs
        fav_btn = tk.Button(hdr, text="★" if is_fav else "☆",
                             bg="white",
                             fg="#F59E0B" if is_fav else "#CBD5E1",
                             font=("Segoe UI", 14), relief="flat",
                             cursor="hand2",
                             command=lambda i=item: self._toggle_fav(i["term"]))
        fav_btn.pack(side="right")

        tk.Label(hdr, text=item["term"], bg="white", fg="#1E293B",
                 font=("Segoe UI", 13, "bold")).pack(side="left")

        # category badge
        if "category" in item:
            tk.Label(hdr, text=item["category"],
                     bg="#EDE9FE", fg="#6D28D9",
                     font=("Segoe UI", 8), padx=6, pady=2,
                     relief="solid", bd=1).pack(side="left", padx=8)

        # definition
        tk.Label(card, text=item["definition"],
                 bg="white", fg="#374151",
                 font=("Segoe UI", 10),
                 wraplength=780, justify="left",
                 padx=12, pady=4).pack(fill="x", anchor="w")

        # formula if present
        if "formula" in item:
            f_frame = tk.Frame(card, bg="#F0FDF4", relief="solid", bd=1)
            f_frame.pack(fill="x", padx=12, pady=(2,4))
            tk.Label(f_frame, text="  📐 Formula: " + item["formula"],
                     bg="#F0FDF4", fg="#166534",
                     font=("Courier New", 10, "bold"),
                     padx=8, pady=4, anchor="w").pack(fill="x")

        # example if present
        if "example" in item:
            ex_frame = tk.Frame(card, bg="#FFFBEB", relief="solid", bd=1)
            ex_frame.pack(fill="x", padx=12, pady=(0,8))
            tk.Label(ex_frame, text="  💡 Example: " + item["example"],
                     bg="#FFFBEB", fg="#92400E",
                     font=("Segoe UI", 9, "italic"),
                     padx=8, pady=4, anchor="w",
                     wraplength=740, justify="left").pack(fill="x")

    def _toggle_fav(self, term):
        if term in self.favs:
            self.favs.remove(term)
        else:
            self.favs.append(term)
        save_favs(self.favs)
        # refresh current view
        if self.cur_subject:
            self.show_subject(self.cur_cycle, self.cur_subject)
        else:
            self.show_favs()

    def show_favs(self):
        self._clear()
        tk.Label(self.content, text="⭐ Your Favorites",
                 bg="#F8F9FA", fg="#1E293B",
                 font=("Segoe UI", 16, "bold")).pack(pady=(20,4), padx=20, anchor="w")

        if not self.favs:
            tk.Label(self.content,
                     text="No favorites yet.\nClick ☆ on any term to save it here!",
                     bg="#F8F9FA", fg="#64748B",
                     font=("Segoe UI", 12)).pack(pady=40)
            return

        for cycle, subjects in self.all_data.items():
            for subject, terms in subjects.items():
                for item in terms:
                    if item["term"] in self.favs:
                        sub_lbl = tk.Label(self.content,
                                           text=f"  {SUBJECT_ICONS.get(subject,'📖')} {subject}  ({cycle})",
                                           bg="#F8F9FA", fg="#6B7280",
                                           font=("Segoe UI", 9))
                        sub_lbl.pack(anchor="w", padx=16)
                        self._term_card(self.content, item, cycle, subject)

    # ── Search ────────────────────────────────────────────────────────────────

    def do_search(self):
        query = self.search_var.get().strip().lower()
        if not query:
            return
        self._clear()
        tk.Label(self.content, text=f'🔍 Results for "{query}"',
                 bg="#F8F9FA", fg="#1E293B",
                 font=("Segoe UI", 14, "bold")).pack(pady=(16,4), padx=20, anchor="w")
        found = 0
        for cycle, subjects in self.all_data.items():
            for subject, terms in subjects.items():
                for item in terms:
                    if (query in item["term"].lower() or
                            query in item["definition"].lower() or
                            query in item.get("formula","").lower() or
                            query in item.get("example","").lower()):
                        lbl = tk.Label(self.content,
                                       text=f"  {SUBJECT_ICONS.get(subject,'📖')} {subject}  ({cycle})",
                                       bg="#F8F9FA", fg="#6B7280",
                                       font=("Segoe UI", 9))
                        lbl.pack(anchor="w", padx=16)
                        self._term_card(self.content, item, cycle, subject)
                        found += 1
        if not found:
            tk.Label(self.content,
                     text="No terms found. Try a different keyword.",
                     bg="#F8F9FA", fg="#64748B",
                     font=("Segoe UI", 12)).pack(pady=30)

    # ── Quiz ──────────────────────────────────────────────────────────────────

    def show_quiz(self):
        self._clear()
        self.quiz_score = [0, 0]

        tk.Label(self.content, text="🧠 Quiz Mode",
                 bg="#F8F9FA", fg="#1E293B",
                 font=("Segoe UI", 16, "bold")).pack(pady=(20,4), padx=20, anchor="w")
        tk.Label(self.content,
                 text="Test your engineering knowledge! Choose the correct definition.",
                 bg="#F8F9FA", fg="#64748B",
                 font=("Segoe UI", 11)).pack(padx=20, anchor="w", pady=(0,12))

        self.quiz_frame = tk.Frame(self.content, bg="#F8F9FA")
        self.quiz_frame.pack(fill="both", expand=True, padx=20)

        self.score_var = tk.StringVar(value="Score: 0 / 0")
        tk.Label(self.content, textvariable=self.score_var,
                 bg="#F8F9FA", fg="#3B82F6",
                 font=("Segoe UI", 12, "bold")).pack(pady=6)

        self._next_question()

    def _next_question(self):
        for w in self.quiz_frame.winfo_children():
            w.destroy()

        # pick random term
        all_terms = [(cycle, subj, item)
                     for cycle, subjects in self.all_data.items()
                     for subj, terms in subjects.items()
                     for item in terms]
        if len(all_terms) < 4:
            tk.Label(self.quiz_frame, text="Not enough terms for quiz.",
                     bg="#F8F9FA").pack()
            return

        correct_cycle, correct_subj, correct = random.choice(all_terms)
        others = random.sample([t for t in all_terms if t[2]["term"] != correct["term"]], 3)
        options = [correct] + others
        random.shuffle(options)

        tk.Label(self.quiz_frame,
                 text=f'What is the definition of:\n"{correct["term"]}"?',
                 bg="white", fg="#1E293B",
                 font=("Segoe UI", 13, "bold"),
                 relief="solid", bd=1,
                 padx=16, pady=16,
                 wraplength=700, justify="center").pack(fill="x", pady=(0,12))

        self.feedback_var = tk.StringVar()
        tk.Label(self.quiz_frame, textvariable=self.feedback_var,
                 bg="#F8F9FA", font=("Segoe UI", 11, "bold"),
                 fg="#059669").pack(pady=4)

        for i, (cyc, sub, opt) in enumerate(options):
            btn = tk.Button(self.quiz_frame,
                            text=f"{chr(65+i)}.  {opt['definition'][:120]}...",
                            bg="white", fg="#374151",
                            font=("Segoe UI", 10),
                            relief="solid", bd=1,
                            padx=10, pady=8,
                            wraplength=680, justify="left",
                            cursor="hand2",
                            command=lambda o=opt, c=correct: self._check_answer(o, c))
            btn.pack(fill="x", pady=4)

        tk.Button(self.quiz_frame, text="Skip →",
                  bg="#F1F5F9", fg="#64748B",
                  font=("Segoe UI", 10), relief="flat",
                  padx=12, pady=4, cursor="hand2",
                  command=self._next_question).pack(pady=(8,0))

    def _check_answer(self, chosen, correct):
        self.quiz_score[1] += 1
        if chosen["term"] == correct["term"]:
            self.quiz_score[0] += 1
            self.feedback_var.set("✅ Correct!")
        else:
            self.feedback_var.set(f"❌ Wrong! Answer: {correct['term']}")
        self.score_var.set(f"Score: {self.quiz_score[0]} / {self.quiz_score[1]}")
        self.after(1800, self._next_question)


if __name__ == "__main__":
    app = EnggDictApp()
    app.mainloop()
