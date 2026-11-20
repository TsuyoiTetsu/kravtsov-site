#!/usr/bin/env bash
set -Eeuo pipefail

# Запускайте из корня проекта: bash deploy.sh
PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

if ! command -v docker >/dev/null 2>&1; then
  echo "Ошибка: Docker не найден. Установите Docker Desktop или Docker Engine." >&2
  exit 1
fi

if ! docker info >/dev/null 2>&1; then
  echo "Ошибка: Docker Engine не запущен или недоступен." >&2
  exit 1
fi

if ! docker compose version >/dev/null 2>&1; then
  echo "Ошибка: Docker Compose v2 недоступен (команда docker compose)." >&2
  exit 1
fi

echo "Сборка образа и запуск контейнера..."
docker compose up -d --build

echo "Ожидание успешной проверки /health..."

for ((attempt = 1; attempt <= 45; attempt++)); do
  container_id="$(docker compose ps -q --all web 2>/dev/null || true)"

  if [[ -z "$container_id" ]]; then
    echo "Контейнер web ещё не создан. Попытка $attempt/45"
    sleep 2
    continue
  fi

  state="$(docker inspect \
    --format='{{.State.Status}}' \
    "$container_id" 2>/dev/null || true)"

  health="$(docker inspect \
    --format='{{if .State.Health}}{{.State.Health.Status}}{{else}}not-configured{{end}}' \
    "$container_id" 2>/dev/null || true)"

  if [[ "$state" == "exited" || "$state" == "dead" ]]; then
    echo "Ошибка: контейнер завершил работу (статус: $state)."
    break
  fi

  case "$health" in
    healthy)
      echo "Готово: приложение доступно по адресу http://localhost:8016"
      echo "Проверка: http://localhost:8016/health"
      exit 0
      ;;

    unhealthy)
      echo "Ошибка: healthcheck завершился со статусом unhealthy."
      break
      ;;

    not-configured)
      echo "Ошибка: для контейнера не настроен healthcheck."
      echo "Проверьте compose.yaml."
      exit 1
      ;;

    *)
      echo "Ожидание healthcheck: статус=$health, контейнер=$state ($attempt/45)"
      ;;
  esac

  sleep 2
done

echo "Ошибка: контейнер не прошёл healthcheck. Последние логи:" >&2
docker compose ps --all
docker compose logs --tail=100 web || true
exit 1