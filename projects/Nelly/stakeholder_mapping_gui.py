import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt

class Stakeholder:
    def __init__(self, name, influence, impact):
        self.name = name
        self.influence = influence
        self.impact = impact

class StakeholderMapping:
    def __init__(self):
        self.stakeholders = []

    def add_stakeholder(self, stakeholder):
        self.stakeholders.append(stakeholder)

    def classify_stakeholders(self):
        categories = {
            "High Influence / High Impact": [],
            "High Influence / Low Impact": [],
            "Low Influence / High Impact": [],
            "Low Influence / Low Impact": []
        }
        
        for stakeholder in self.stakeholders:
            if stakeholder.influence >= 3 and stakeholder.impact >= 3:
                categories["High Influence / High Impact"].append(stakeholder)
            elif stakeholder.influence >= 3 and stakeholder.impact < 3:
                categories["High Influence / Low Impact"].append(stakeholder)
            elif stakeholder.influence < 3 and stakeholder.impact >= 3:
                categories["Low Influence / High Impact"].append(stakeholder)
            else:
                categories["Low Influence / Low Impact"].append(stakeholder)
        
        return categories

class StakeholderInputDialog(simpledialog.Dialog):
    def __init__(self, parent, title, name):
        self.name = name
        self.influence = None
        self.impact = None
        super().__init__(parent, title)

    def body(self, master):
        tk.Label(master, text=f"Influence Level for {self.name} (1-5):").grid(row=0)
        self.influence_scale = tk.Scale(master, from_=1, to=5, orient=tk.HORIZONTAL)
        self.influence_scale.grid(row=0, column=1)

        tk.Label(master, text=f"Impact Level for {self.name} (1-5):").grid(row=1)
        self.impact_scale = tk.Scale(master, from_=1, to=5, orient=tk.HORIZONTAL)
        self.impact_scale.grid(row=1, column=1)

        # return self.influence_scale

    def apply(self):
        self.influence = self.influence_scale.get()
        self.impact = self.impact_scale.get()

def plot_results(categories):
    fig, axs = plt.subplots(2, 2, figsize=(10, 10), sharex=True, sharey=True)

    colors = {
        "High Influence / High Impact": "#FD7052",
        "High Influence / Low Impact": "#F0FD52",
        "Low Influence / High Impact": "#FD60D2",
        "Low Influence / Low Impact": "#7195FD"
    }

    for ax, (category, stakeholders) in zip(axs.flat, categories.items()):
        influence_values = [stakeholder.influence for stakeholder in stakeholders]
        impact_values = [stakeholder.impact for stakeholder in stakeholders]
        ax.scatter(influence_values, impact_values, color='black', marker='o', alpha=0.7, s=400)
        ax.set_title(category)
        ax.set_xlabel('Influence')
        ax.set_ylabel('Impact')
        ax.grid(True)
        ax.set_facecolor(colors[category])  
    
    plt.suptitle('Stakeholder Map', fontsize=16)
    plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])

    plt.show()

def main():
    stakeholder_mapping = StakeholderMapping()

    stakeholders = [
        {"name": "Ostap"},
        {"name": "Maria"},
        {"name": "Taras"},
        {"name": "Oksana"},
        {"name": "Ivan"}
    ]

    root = tk.Tk()
    root.withdraw()

    for stakeholder_data in stakeholders:
        dialog = StakeholderInputDialog(root, f"Stakeholder Data Entry - {stakeholder_data['name']}", stakeholder_data['name'])
        stakeholder = Stakeholder(stakeholder_data['name'], dialog.influence, dialog.impact)
        stakeholder_mapping.add_stakeholder(stakeholder)

    categories = stakeholder_mapping.classify_stakeholders()
    
    result_message = "\nStakeholder Results:"
    for category, names in categories.items():
        result_message += f"\n\n{category}:"
        for stakeholder in names:
            result_message += f"\n - {stakeholder.name}"
    
    messagebox.showinfo("Results", result_message)
    
    plot_results(categories)

if __name__ == "__main__":
    main()