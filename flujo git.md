# Flujo Git — Sparse Checkout

## Inicialización

```bash
cd "C:\Users\ingga\OneDrive\Documentos\Nueva carpeta\Clases"
git init
git remote add origin https://github.com/gaaguirrer/Clases
git config core.sparseCheckout true
git config core.sparseCheckoutCone false
```

Escribir en `.git\info\sparse-checkout` las carpetas deseadas con `/**` al final:

```
Administración de Sistemas de Información/**
Gerencia de Operaciones I/**
Sistemas electrónicos/**
Ingeniería del Software I/**
Libre I (SPSS)/**
Marketing Digital/**
Diseño de Bases de Datos/**
Ingeniería del software III/**
Gestión de Proyectos Tecnológicos/**
Optativa profesional II (gobernanza y Criptografía)/**
```

Luego:
```bash
git clone --sparse --filter=blob:none --depth 1 https://github.com/gaaguirrer/Clases
git read-tree -mu HEAD
```

---

## Agregar carpeta nueva

```bash
# Agregar patrón a .git/info/sparse-checkout
git read-tree -mu HEAD
```

## Quitar carpeta de mi PC (sin borrarla de GitHub)

```bash
# Quitar la línea de .git/info/sparse-checkout
git read-tree -mu HEAD
Remove-Item -Recurse -Force carpeta
```

## Actualizar todo

```bash
git pull
```

---

## Carpetas descargadas actualmente

- Administración de Sistemas de Información
- Gerencia de Operaciones I
- Sistemas electrónicos
- Ingeniería del Software I
- Libre I (SPSS)
- Marketing Digital
- Diseño de Bases de Datos
- Ingeniería del software III
- Gestión de Proyectos Tecnológicos
- Optativa profesional II (gobernanza y Criptografía)
