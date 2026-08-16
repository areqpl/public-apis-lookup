#!/usr/bin/env bash
# ==============================================================================
# Universal Installer for public-apis-lookup skill & CLI tool
# Compatible with: Antigravity CLI, Claude Code, Cursor, Windsurf, Aider, Bash
# ==============================================================================

set -e

REPO_RAW_URL="https://raw.githubusercontent.com/areqpl/public-apis-lookup/main"
SKILL_NAME="public-apis-lookup"
TARGET_DIR="${HOME}/.agents/skills/${SKILL_NAME}"
BIN_DIR="${HOME}/.local/bin"
SCRIPT_SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd || echo "")"

echo "==> Installing ${SKILL_NAME}..."

# 1. Ensure target directories exist
mkdir -p "${TARGET_DIR}/scripts"
mkdir -p "${TARGET_DIR}/resources"
mkdir -p "${BIN_DIR}"

# 2. Deploy files
if [ -n "${SCRIPT_SRC_DIR}" ] && [ -f "${SCRIPT_SRC_DIR}/scripts/query_apis.py" ] && [ "${SCRIPT_SRC_DIR}" != "${TARGET_DIR}" ]; then
    echo "--> Copying files from local source (${SCRIPT_SRC_DIR})..."
    cp -r "${SCRIPT_SRC_DIR}/SKILL.md" "${TARGET_DIR}/" 2>/dev/null || true
    cp -r "${SCRIPT_SRC_DIR}/scripts/"* "${TARGET_DIR}/scripts/" 2>/dev/null || true
    cp -r "${SCRIPT_SRC_DIR}/resources/"* "${TARGET_DIR}/resources/" 2>/dev/null || true
    [ -f "${SCRIPT_SRC_DIR}/README.md" ] && cp "${SCRIPT_SRC_DIR}/README.md" "${TARGET_DIR}/" 2>/dev/null || true
elif [ ! -f "${TARGET_DIR}/scripts/query_apis.py" ] || [ ! -f "${TARGET_DIR}/resources/public_apis.json" ]; then
    echo "--> Downloading files from GitHub repository..."
    curl -sSL "${REPO_RAW_URL}/SKILL.md" -o "${TARGET_DIR}/SKILL.md"
    curl -sSL "${REPO_RAW_URL}/scripts/query_apis.py" -o "${TARGET_DIR}/scripts/query_apis.py"
    curl -sSL "${REPO_RAW_URL}/resources/public_apis.json" -o "${TARGET_DIR}/resources/public_apis.json"
    curl -sSL "${REPO_RAW_URL}/README.md" -o "${TARGET_DIR}/README.md" 2>/dev/null || true
fi

# 3. Set executable permissions
chmod +x "${TARGET_DIR}/scripts/query_apis.py"

# 4. Create global CLI symlink
ln -sf "${TARGET_DIR}/scripts/query_apis.py" "${BIN_DIR}/public-apis"

echo "==> Installation complete!"
echo "    - Skill location: ${TARGET_DIR}"
echo "    - CLI executable: ${BIN_DIR}/public-apis"

# 5. Check if ~/.local/bin is in PATH
if [[ ":$PATH:" != *":${BIN_DIR}:"* ]]; then
    echo ""
    echo "⚠️  Note: ${BIN_DIR} is not in your current PATH."
    echo "   Add it to your shell config (~/.bashrc, ~/.zshrc):"
    echo "   export PATH=\"\$HOME/.local/bin:\$PATH\""
fi

# 6. Verify installation
echo ""
echo "==> Verifying installation:"
"${TARGET_DIR}/scripts/query_apis.py" -q "meteo" --limit 1

echo ""
echo "🎉 Ready! Run 'public-apis --help' or ask your AI agent to find APIs."
