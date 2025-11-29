class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Node({self.key})"


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """Вставка одного елемента"""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
    
    def search(self, key):
        """Пошук елемента"""
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)
    
    def insert_subtree(self, subtree_root):
        """Вставка піддерева в наявне дерево"""
        if subtree_root is None:
            return
        # Вставляємо корінь піддерева
        self.insert(subtree_root.key)
        # Рекурсивно вставляємо ліве та праве піддерево
        self.insert_subtree(subtree_root.left)
        self.insert_subtree(subtree_root.right)
    
    def delete_subtree(self, key):
        """Видалення піддерева за ключем кореня піддерева"""
        if self.root is None:
            return False
        
        # Якщо видаляємо корінь всього дерева
        if self.root.key == key:
            self.root = None
            return True
        
        # Шукаємо батьківський вузол
        return self._delete_subtree_recursive(self.root, key)
    
    def _delete_subtree_recursive(self, node, key):
        if node is None:
            return False
        
        # Перевіряємо ліву дитину
        if node.left and node.left.key == key:
            node.left = None
            return True
        
        # Перевіряємо праву дитину
        if node.right and node.right.key == key:
            node.right = None
            return True
        
        # Рекурсивно шукаємо далі
        if key < node.key:
            return self._delete_subtree_recursive(node.left, key)
        else:
            return self._delete_subtree_recursive(node.right, key)
    
    def print_tree(self, node=None, level=0, prefix="Root: "):
        """Візуалізація дерева"""
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- (empty)")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- (empty)")


# === ДЕМОНСТРАЦІЯ ПРОГРАМИ МІНІМУМ ===
print("=" * 50)
print("ПРОГРАМА МІНІМУМ: Вставка та видалення піддерев")
print("=" * 50)

# Створюємо основне дерево
bst = BinarySearchTree()
for key in [8, 3, 10, 1, 6, 14]:
    bst.insert(key)

print("\n1. Початкове дерево:")
bst.print_tree()

# Створюємо піддерево для вставки
subtree = Node(20)
subtree.left = Node(17)
subtree.right = Node(25)

print("\n2. Піддерево для вставки (корінь 20):")
print("    20")
print("   /  \\")
print("  17  25")

# Вставляємо піддерево
bst.insert_subtree(subtree)
print("\n3. Дерево після вставки піддерева:")
bst.print_tree()

# Видаляємо піддерево
print("\n4. Видаляємо піддерево з коренем 10:")
bst.delete_subtree(10)
bst.print_tree()


# ============================================================
# ПРОГРАМА МАКСИМУМ: HTML Парсер
# ============================================================

import re
from typing import Optional, List


class DOMNode:
    """Вузол DOM дерева"""
    def __init__(self, tag: str, text: str = ""):
        self.tag = tag
        self.text = text
        self.children: List['DOMNode'] = []
        self.parent: Optional['DOMNode'] = None
    
    def add_child(self, child: 'DOMNode'):
        child.parent = self
        self.children.append(child)
    
    def __repr__(self):
        return f"DOMNode(tag='{self.tag}', text='{self.text[:20]}...' if len(self.text) > 20 else '{self.text}')"


class HTMLParser:
    """Парсер HTML документів"""
    
    # Самозакриваючі теги
    SELF_CLOSING_TAGS = {'br', 'hr', 'img', 'input', 'meta', 'link', 'area', 'base', 'col', 'embed', 'source', 'track', 'wbr'}
    
    def __init__(self):
        self.root: Optional[DOMNode] = None
    
    def parse(self, html: str) -> DOMNode:
        """Парсинг HTML документа та побудова DOM дерева"""
        # Очищуємо HTML від зайвих пробілів
        html = re.sub(r'\s+', ' ', html).strip()
        
        # Створюємо кореневий вузол
        self.root = DOMNode("document")
        
        # Парсимо HTML
        self._parse_content(html, self.root)
        
        return self.root
    
    def _parse_content(self, html: str, parent: DOMNode):
        """Рекурсивний парсинг HTML контенту"""
        position = 0
        
        while position < len(html):
            # Шукаємо наступний тег
            tag_start = html.find('<', position)
            
            if tag_start == -1:
                # Більше немає тегів, додаємо залишок як текст
                text = html[position:].strip()
                if text:
                    parent.text += " " + text if parent.text else text
                break
            
            # Додаємо текст перед тегом
            text_before = html[position:tag_start].strip()
            if text_before:
                parent.text += " " + text_before if parent.text else text_before
            
            # Знаходимо кінець тегу
            tag_end = html.find('>', tag_start)
            if tag_end == -1:
                break
            
            tag_content = html[tag_start + 1:tag_end]
            
            # Пропускаємо коментарі та DOCTYPE
            if tag_content.startswith('!'):
                position = tag_end + 1
                continue
            
            # Перевіряємо чи це закриваючий тег
            if tag_content.startswith('/'):
                position = tag_end + 1
                continue
            
            # Витягуємо ім'я тегу
            tag_name = tag_content.split()[0].lower().rstrip('/')
            
            # Перевіряємо чи це самозакриваючий тег
            is_self_closing = tag_name in self.SELF_CLOSING_TAGS or tag_content.endswith('/')
            
            # Створюємо новий вузол
            new_node = DOMNode(tag_name)
            parent.add_child(new_node)
            
            if is_self_closing:
                position = tag_end + 1
            else:
                # Шукаємо закриваючий тег
                close_tag = f'</{tag_name}>'
                close_pos = self._find_closing_tag(html, tag_end + 1, tag_name)
                
                if close_pos != -1:
                    # Рекурсивно парсимо вміст тегу
                    inner_content = html[tag_end + 1:close_pos]
                    self._parse_content(inner_content, new_node)
                    position = close_pos + len(close_tag)
                else:
                    position = tag_end + 1
    
    def _find_closing_tag(self, html: str, start: int, tag_name: str) -> int:
        """Знаходить позицію закриваючого тегу з урахуванням вкладеності"""
        depth = 1
        position = start
        open_tag = f'<{tag_name}'
        close_tag = f'</{tag_name}>'
        
        while position < len(html) and depth > 0:
            next_open = html.lower().find(open_tag, position)
            next_close = html.lower().find(close_tag, position)
            
            if next_close == -1:
                return -1
            
            if next_open != -1 and next_open < next_close:
                # Знайдено вкладений відкриваючий тег
                depth += 1
                position = next_open + len(open_tag)
            else:
                # Знайдено закриваючий тег
                depth -= 1
                if depth == 0:
                    return next_close
                position = next_close + len(close_tag)
        
        return -1
    
    def find_by_tag(self, tag: str) -> List[DOMNode]:
        """Пошук всіх вузлів за тегом"""
        results = []
        self._find_by_tag_recursive(self.root, tag.lower(), results)
        return results
    
    def _find_by_tag_recursive(self, node: DOMNode, tag: str, results: List[DOMNode]):
        """Рекурсивний пошук за тегом"""
        if node is None:
            return
        
        if node.tag == tag:
            results.append(node)
        
        for child in node.children:
            self._find_by_tag_recursive(child, tag, results)
    
    def get_text_by_tag(self, tag: str) -> List[str]:
        """Отримати текст за тегом"""
        nodes = self.find_by_tag(tag)
        texts = []
        for node in nodes:
            all_text = self._collect_all_text(node)
            if all_text:
                texts.append(all_text)
        return texts
    
    def _collect_all_text(self, node: DOMNode) -> str:
        """Збирає весь текст з вузла та його дітей"""
        text_parts = []
        if node.text:
            text_parts.append(node.text)
        for child in node.children:
            child_text = self._collect_all_text(child)
            if child_text:
                text_parts.append(child_text)
        return ' '.join(text_parts)
    
    def print_tree(self, node: Optional[DOMNode] = None, level: int = 0):
        """Візуалізація DOM дерева"""
        if node is None:
            node = self.root
        
        indent = "  " * level
        text_preview = node.text[:30] + "..." if len(node.text) > 30 else node.text
        print(f"{indent}<{node.tag}>{' → \"' + text_preview + '\"' if node.text else ''}")
        
        for child in node.children:
            self.print_tree(child, level + 1)


# === ДЕМОНСТРАЦІЯ ПРОГРАМИ МАКСИМУМ ===
print("\n" + "=" * 50)
print("ПРОГРАМА МАКСИМУМ: HTML Парсер з DOM деревом")
print("=" * 50)

# Тестовий HTML документ
html_doc = """
<!DOCTYPE html>
<html>
<head>
    <title>Тестова сторінка</title>
</head>
<body>
    <div>
        <h1>Привіт, світе!</h1>
        <p>Це перший параграф тексту.</p>
        <p>А це другий параграф з <strong>жирним</strong> текстом.</p>
    </div>
    <div>
        <h2>Підзаголовок</h2>
        <ul>
            <li>Пункт 1</li>
            <li>Пункт 2</li>
            <li>Пункт 3</li>
        </ul>
    </div>
</body>
</html>
"""

# Парсимо HTML
parser = HTMLParser()
dom = parser.parse(html_doc)

print("\n1. Структура DOM дерева:")
print("-" * 40)
parser.print_tree()

print("\n2. Пошук тексту за тегом:")
print("-" * 40)

# Пошук за різними тегами
tags_to_search = ['title', 'h1', 'h2', 'p', 'li', 'strong']

for tag in tags_to_search:
    texts = parser.get_text_by_tag(tag)
    print(f"\n<{tag}>:")
    if texts:
        for text in texts:
            print(f"  → {text}")
    else:
        print("  (текст не знайдено)")

# Функція пошуку
print("\n" + "=" * 50)
print("3. Приклад функції пошуку:")
print("-" * 40)

def search_html(html: str, tag: str) -> List[str]:
    """
    Функція пошуку тексту за тегом
    Вхідні дані: html документ та тег
    Вихідні дані: список текстів або порожній список
    """
    parser = HTMLParser()
    parser.parse(html)
    return parser.get_text_by_tag(tag)

# Демонстрація
result = search_html(html_doc, "p")
print(f"search_html(html_doc, 'p') = {result}")

result = search_html(html_doc, "li")
print(f"search_html(html_doc, 'li') = {result}")
