# DevOps වලදී අපි හැමදාම කරන දෙයක්.
# Install කරන්න ඕන packages ලැයිස්තුවක්.
packages_to_install = ["nginx", "docker", "git", "vim"]

# දැන් අපි මේ ලැයිස්තුවේ තියෙන හැම package එකක්ම install කරන්න ඕනේ.
print("\n--- Starting package installation ---")

# මෙන්න loop එක
for package in packages_to_install:
    # 1 වෙනි වටය: `package` කියන variable එකේ value එක "nginx" වෙනවා.
    # 2 වෙනි වටය: `package` කියන variable එකේ value එක "docker" වෙනවා.
    # 3 වෙනි වටය: `package` කියන variable එකේ value එක "git" වෙනවා.
    # 4 වෙනි වටය: `package` කියන variable එකේ value එක "vim" වෙනවා.
    # ලැයිස්තුව ඉවරයි. loop එක නවතිනවා.
    
    # හැම වටයකදීම මේ f-string එක print වෙනවා.
    print(f"Running command: sudo apt-get install {package}")

print("--- All packages installed ---")