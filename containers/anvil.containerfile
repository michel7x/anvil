# Build from the repository root with any OCI engine:
#   docker build -f containers/anvil.containerfile -t anvil .
#   podman build -f containers/anvil.containerfile -t anvil .

ARG PYTHON_VERSION=3.14
ARG UV_VERSION=0.13.7

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv

FROM docker.io/library/python:${PYTHON_VERSION}-slim-trixie AS builder
COPY --from=uv /uv /usr/local/bin/uv
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never
WORKDIR /app

# Dependencies first, so source edits don't invalidate this layer.
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project --no-editable

COPY README.md LICENSE ./
COPY src ./src
RUN uv sync --locked --no-dev --no-editable

FROM docker.io/library/python:${PYTHON_VERSION}-slim-trixie AS runtime
LABEL org.opencontainers.image.title="anvil" \
      org.opencontainers.image.description="Forge context-engineering scaffolds for AI coding agents." \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.source="https://github.com/michel7x/anvil"

RUN useradd --uid 1000 --create-home nonroot \
    && install -d -o nonroot -g nonroot /work
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:${PATH}"

USER 1000
WORKDIR /work
ENTRYPOINT ["anvil"]
CMD ["--help"]
