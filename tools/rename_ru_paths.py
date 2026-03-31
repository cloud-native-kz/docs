#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import subprocess
from pathlib import Path


TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"(!?\[([^\]]*)\])\(([^)]+)\)")

SKIP_FILE_NAMES = {"README.md", "index.md"}
SKIP_DIR_NAMES = {"ru", "css", "mps", "trtc", "биллинг", "начало-работы"}
SKIP_PREFIXES = (
    "describe",
    "create",
    "delete",
    "modify",
    "update",
    "enable",
    "forbid",
    "resume",
    "restart",
    "start",
    "stop",
    "add",
    "remove",
    "unbind",
    "authenticate",
    "drop",
)

SEGMENT_MAP = {
    "about-pushing": "о-потоковой-публикации",
    "account-system": "система-аккаунтов",
    "activate-the-service": "активация-сервиса",
    "advanced-features": "расширенные-возможности",
    "all-platform": "все-платформы",
    "announcements": "объявления",
    "api-documentation": "документация-api",
    "api-reference": "справочник-api",
    "application-scenario-and-practical-tutorial": "сценарии-применения-и-практические-руководства",
    "best-practices": "лучшие-практики",
    "call-records": "записи-звонков",
    "call-status-webhooks": "вебхуки-статуса-звонков",
    "client-apis": "клиентские-api",
    "cloud-search": "облачный-поиск",
    "community-and-topic": "сообщества-и-топики",
    "console-guide": "руководство-по-консоли",
    "conversation-group": "группа-разговоров",
    "conversation-list": "список-разговоров",
    "core-sdk": "core-sdk",
    "css-policy": "политики-css",
    "customize-styles": "настройка-стилей",
    "data-processing-and-security-agreement": "соглашение-об-обработке-данных-и-безопасности",
    "domain-management": "управление-доменами",
    "engine-apis": "api-движка",
    "faqs": "частые-вопросы",
    "feature-configuration": "настройка-возможностей",
    "feature-guide": "руководство-по-возможностям",
    "features": "возможности",
    "following-and-fans-related-webhooks": "вебхуки-подписок-и-подписчиков",
    "get-started": "быстрый-старт",
    "getting-started": "начало-работы",
    "global-mute-management": "глобальное-управление-выключением-звука",
    "group-custom-attributes": "пользовательские-атрибуты-группы",
    "group-information": "информация-о-группе",
    "group-management": "управление-группой",
    "group-member-information": "информация-об-участниках-группы",
    "group-member-management": "управление-участниками-группы",
    "group-related": "связанные-с-группами",
    "historical-message": "исторические-сообщения",
    "init-and-login": "инициализация-и-вход",
    "integration-tutorials": "интеграционные-руководства",
    "legacy-documents": "устаревшие-документы",
    "live-recording": "запись-прямого-эфира",
    "live-stream-management-apis": "api-управления-прямыми-эфирами",
    "live-stream-mix-apis": "api-микширования-потоков",
    "live-streaming-security": "безопасность-прямых-эфиров",
    "making-api-request": "выполнение-api-запроса",
    "making-api-requests": "выполнение-api-запросов",
    "manufacturer-channel": "каналы-производителей",
    "manufacturer-configuration": "настройка-производителей",
    "message-extension": "расширение-сообщений",
    "message-management": "управление-сообщениями",
    "message-related": "связанные-с-сообщениями",
    "monitoring-dashboard": "панель-мониторинга",
    "offline-call-push": "офлайн-push-звонков",
    "official-channel-management": "управление-официальными-каналами",
    "official-channel-related": "связанные-с-официальными-каналами",
    "on-cloud-recording-apis": "api-облачной-записи",
    "online-status-webhooks": "вебхуки-онлайн-статуса",
    "operations-management": "управление-операциями",
    "operations-management-callbacks": "колбэки-управления-операциями",
    "ops-guide": "руководство-по-эксплуатации",
    "other-apis": "прочие-api",
    "other-documents": "прочие-документы",
    "other-tutorials": "прочие-руководства",
    "pay-as-you-go": "оплата-по-мере-использования",
    "pc-push": "публикация-с-пк",
    "playing-method": "способы-воспроизведения",
    "playback-domain-name-management": "управление-доменами-воспроизведения",
    "practice-solutions": "практические-решения",
    "practices-in-typical-scenarios": "практики-в-типовых-сценариях",
    "pricing": "цены",
    "privacy-policy": "политика-конфиденциальности",
    "privacy-sla": "конфиденциальность-и-sla",
    "product-features": "возможности-продукта",
    "product-introduction": "обзор-продукта",
    "product-information": "информация-о-продукте",
    "purchase-guide": "руководство-по-покупке",
    "push-and-playback": "публикация-и-воспроизведение",
    "push-callback": "колбэк-публикации",
    "push-domain-name-management": "управление-доменами-публикации",
    "push-service": "push-сервис",
    "quick-integration": "быстрая-интеграция",
    "quick-integration-guide": "руководство-по-быстрой-интеграции",
    "read-receipt": "прочтение",
    "recording-management-apis": "api-управления-записью",
    "related-agreement": "связанные-соглашения",
    "release-notes": "примечания-к-выпуску",
    "release-notes-and-announcements": "примечания-к-выпуску-и-объявления",
    "relationship-chain-webhooks": "вебхуки-цепочки-связей",
    "rest-api": "rest-api",
    "restful-api": "restful-api",
    "room-management": "управление-комнатами",
    "room-management-apis": "api-управления-комнатами",
    "room-related": "связанные-с-комнатами",
    "rtc-analytics": "rtc-аналитика",
    "rtc-engine": "rtc-engine",
    "scenario-based-practice": "практика-на-основе-сценариев",
    "sdk-guide": "руководство-sdk",
    "seat-connection-related": "связанные-с-подключением-мест",
    "seat-management": "управление-местами",
    "search-messages": "поиск-сообщений",
    "self-diagnosis": "самодиагностика",
    "send-message": "отправка-сообщений",
    "server-apis": "серверные-api",
    "server-features": "серверные-возможности",
    "session-grouping-tag": "теги-группировки-сессий",
    "session-related": "связанные-с-сессиями",
    "session-unread-count": "непрочитанное-в-сессиях",
    "service-level-agreement": "соглашение-об-уровне-сервиса",
    "sla": "sla",
    "social-entertainment": "социальные-развлечения",
    "stream-pulling-apis": "api-вытягивания-потока",
    "streamlinksecurity-group-management-apis": "api-управления-группами-bezopasnosti-streamlink",
    "supplementary-description-of-public-api": "дополнительное-описание-публичного-api",
    "task-management-apis": "api-управления-задачами",
    "tencent-rtc-essentials": "основы-tencent-rtc",
    "third-party-callback": "сторонний-колбэк",
    "time-shifting": "сдвиг-времени",
    "time-shifting-apis": "api-сдвига-времени",
    "toolkit": "инструментарий",
    "troubleshooting": "устранение-неполадок",
    "trtc-policies": "политики-trtc",
    "ui-components": "ui-компоненты",
    "ui-customization": "настройка-ui",
    "uikit-apis": "api-uikit",
    "usage": "использование",
    "user-guides-for-common-third-party-tools": "руководства-по-сторонним-инструментам",
    "user-management": "управление-пользователями",
    "user-profile-and-relationship-chain": "профили-пользователей-и-цепочка-связей",
    "user-related": "связанные-с-пользователями",
    "user-related-matters": "вопросы-пользователей",
    "value-added-service-fee": "тарифы-на-дополнительные-услуги",
    "web-player": "веб-плеер",
    "webhooks": "вебхуки",
    "webhooks-configuration": "настройка-вебхуков",
}

EXCLUDED_SEGMENTS = {
    "api-documentation",
    "api-reference",
    "sdk-guide",
    "server-apis",
    "rest-api",
    "restful-api",
    "uikit",
    "client-apis",
    "engine-apis",
    "core-sdk",
    "rtc-engine",
    "api",
}

EXCLUDED_ROOT_PREFIXES = {
    ("trtc", "call"),
    ("trtc", "chat"),
    ("trtc", "conference"),
    ("trtc", "live"),
    ("trtc", "beauty-ar"),
    ("trtc", "rtc-engine"),
    ("trtc", "server-apis"),
}

def git_mv(repo: Path, src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "-C", str(repo), "mv", str(src), str(dst)], check=True)


def extract_title(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    match = TITLE_RE.search(text)
    if not match:
        return None
    title = match.group(1).strip()
    title = re.sub(r"`([^`]+)`", r"\1", title)
    title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title)
    title = re.sub(r"[*_~]", "", title)
    title = re.sub(r"<[^>]+>", "", title)
    return title.strip()


def slugify(text: str) -> str:
    text = text.lower().replace("ё", "е")
    text = text.replace("&", " и ")
    text = re.sub(r"[/'\"“”‘’(){}[\]:,.!?+]", " ", text)
    text = text.replace("—", " ").replace("–", " ")
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    text = re.sub(r"(^-|-$)", "", text)
    return text


def parse_readme_map(ru_root: Path) -> tuple[dict[Path, str], dict[Path, str]]:
    readme = ru_root / "README.md"
    file_labels: dict[Path, str] = {}
    dir_candidates: dict[Path, set[str]] = {}
    heading_stack: dict[int, str] = {}

    for line in readme.read_text(encoding="utf-8").splitlines():
        heading_match = re.match(r"^(#{2,6})\s+(.+?)\s*$", line)
        if heading_match:
            level = len(heading_match.group(1))
            heading_stack[level] = heading_match.group(2).strip()
            for key in list(heading_stack):
                if key > level:
                    del heading_stack[key]
            continue

        for _, label, target in LINK_RE.findall(line):
            if label == "RU" or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if not clean:
                continue
            rel = Path(clean)
            if not (ru_root / rel).exists():
                continue
            file_labels[rel] = label.strip()
            parts = rel.parts[:-1]
            for depth in range(1, len(parts) + 1):
                if parts and parts[0] == "trtc":
                    continue
                if depth == 1 and parts[0] in {"css", "mps", "trtc"}:
                    continue
                heading = heading_stack.get(depth + 1)
                if heading:
                    dir_candidates.setdefault(Path(*parts[:depth]), set()).add(heading.strip())

    dir_labels = {path: next(iter(labels)) for path, labels in dir_candidates.items() if len(labels) == 1}
    return file_labels, dir_labels


def is_excluded_path(rel: Path) -> bool:
    parts = rel.parts
    if len(parts) >= 2 and tuple(parts[:2]) in EXCLUDED_ROOT_PREFIXES:
        return True
    return any(part in EXCLUDED_SEGMENTS for part in parts)


def should_rename_file(path: Path, title: str | None) -> bool:
    if path.name in SKIP_FILE_NAMES or not title:
        return False
    latin = len(re.findall(r"[A-Za-z]", title))
    cyr = len(re.findall(r"[А-Яа-яЁё]", title))
    base = path.stem.lower()
    if cyr == 0 and (latin > 0 or any(base.startswith(prefix) for prefix in SKIP_PREFIXES)):
        return False
    return True


def target_file_name(path: Path, title: str) -> str:
    slug = slugify(title)
    if not slug:
        return path.name
    return f"{slug}.md"


def build_dir_mapping(ru_root: Path, readme_dir_labels: dict[Path, str]) -> dict[Path, Path]:
    mapping: dict[Path, Path] = {}
    for directory in sorted([p for p in ru_root.rglob("*") if p.is_dir()], key=lambda p: len(p.parts)):
        rel = directory.relative_to(ru_root)
        if is_excluded_path(rel):
            continue
        new_parts = []
        for idx, part in enumerate(rel.parts, start=1):
            if part in SKIP_DIR_NAMES:
                new_parts.append(part)
            elif part in SEGMENT_MAP:
                new_parts.append(SEGMENT_MAP[part])
            else:
                new_parts.append(part)
        new_dir = ru_root.joinpath(*new_parts)
        if new_dir != directory:
            mapping[directory] = new_dir
    return mapping


def remap_parent(path: Path, dir_mapping: dict[Path, Path]) -> Path:
    for depth in range(len(path.parts), 0, -1):
        candidate = Path(*path.parts[:depth])
        if candidate in dir_mapping:
            suffix = path.parts[depth:]
            return dir_mapping[candidate].joinpath(*suffix)
    return path


def build_file_mapping(
    ru_root: Path, dir_mapping: dict[Path, Path], readme_file_labels: dict[Path, str]
) -> dict[Path, Path]:
    mapping: dict[Path, Path] = {}
    collision_guard: dict[Path, int] = {}
    for path in sorted(ru_root.rglob("*.md")):
        title = extract_title(path)
        parent = remap_parent(path.parent, dir_mapping)
        new_name = path.name
        rel = path.relative_to(ru_root)
        if is_excluded_path(rel):
            continue
        label = readme_file_labels.get(rel)
        if label and path.name not in SKIP_FILE_NAMES:
            new_name = f"{slugify(label)}.md"
        elif should_rename_file(path, title):
            new_name = target_file_name(path, title or "")
        target = parent / new_name
        if target == path:
            continue
        unique_target = target
        while unique_target in mapping.values() or (unique_target.exists() and unique_target != path):
            collision_guard[target] = collision_guard.get(target, 1) + 1
            unique_target = target.with_name(f"{target.stem}-{collision_guard[target]}{target.suffix}")
        mapping[path] = unique_target
    return mapping


def rewrite_links(repo: Path, file_mapping: dict[Path, Path]) -> list[Path]:
    changed: list[Path] = []
    for path in repo.rglob("*.md"):
        original = path.read_text(encoding="utf-8")

        def repl(match: re.Match[str]) -> str:
            full_label, _, target = match.groups()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                return match.group(0)
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if not clean:
                return match.group(0)
            resolved = (path.parent / clean).resolve()
            new_target = file_mapping.get(resolved)
            if not new_target:
                return match.group(0)
            rel = os.path.relpath(new_target, path.parent)
            rel = rel.replace(os.sep, "/")
            suffix = target[len(clean):]
            return f"{full_label}({rel}{suffix})"

        updated = LINK_RE.sub(repl, original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(path)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    ru_root = repo / "ru"

    readme_file_labels, readme_dir_labels = parse_readme_map(ru_root)
    dir_mapping = build_dir_mapping(ru_root, readme_dir_labels)
    file_mapping = build_file_mapping(ru_root, dir_mapping, readme_file_labels)

    print(f"dir renames: {len(dir_mapping)}")
    print(f"file renames: {len(file_mapping)}")

    if not args.apply:
        for src, dst in list(dir_mapping.items())[:20]:
            print(f"DIR {src.relative_to(repo)} -> {dst.relative_to(repo)}")
        for src, dst in list(file_mapping.items())[:20]:
            print(f"FILE {src.relative_to(repo)} -> {dst.relative_to(repo)}")
        return

    all_file_moves: dict[Path, Path] = {}
    for path in sorted([p for p in ru_root.rglob("*") if p.is_file()]):
        target_parent = remap_parent(path.parent, dir_mapping)
        target = file_mapping.get(path, target_parent / path.name)
        if target != path:
            all_file_moves[path] = target

    moved_mapping: dict[Path, Path] = {}
    for src, dst in all_file_moves.items():
        if src.exists():
            git_mv(repo, src, dst)
        moved_mapping[src.resolve()] = dst.resolve()

    rewrite_links(repo, moved_mapping)


if __name__ == "__main__":
    main()
