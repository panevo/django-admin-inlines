# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-06-17

### Changed

* Update package details for publishing to PyPi
* Drop support for Python 3.8
* Add support for Python 3.12, 3.13
* Add suport for Django 5.x

## [1.0.1] - 2024-05-28

### Changed

* Modify package details for publishing to PyPi

## [1.0] - 2024-05-22

### Added

* support for django 4.x

### Changed

* dropped support for python below 3.8 as Django 4 requires min 3.8
* removed RemovedInDjango40Warning warning message, thanks to @Ivan-Feofanov

## [2.4.0] - 2021-02-08

### Fixed

* Do not break if `render_inline_actions` field is missing, thanks to @tony

### Added

* support for django 3.x

### Changed

* dropped support for python 3.5

## [2.3.0] - 2019-09-27

* feat: support for intermediat forms, #25
* feat: support for Django 2.2
* feat: support for Python 3.8

## [2.2.0] - 2018-06-13

* feat: support for Django 2.2
* feat: Support multiple inlines for the same related model
* fix: keep original exception, when an action could not be executed

## [2.1.0] - 2018-09-09

* feat: support for django 2.1

## [2.0.2] - 2018-04-12

* fix: load css files on admin pages (thanks @tripliks)

## [2.0.1] - 2018-01-20

* fix: don't show actions on unsaved inlines  (thanks @tripliks)

## [2.0.0] - 2018-01-04

* Add support for django 2.0
* *BREAKING CHANGE* Drop support for python 2.x
* *BREAKING CHANGE* Drop support for django<2.0

## [1.2.0] - 2018-01-04

* Added support for django 1.11
* Dropped support for django 1.7

## [1.1.0] - 2017-07-21

* Add support for per-object label and css classes (thanks to @DimmuR)

## [1.0.0] - 1016-11-12

* *BREAKING CHANGE* support for admin changelist

## [0.1.1] - 2016-09-27

* Fixed duplication of field Actions in inlines (thanks to @torwald-sergesson)

## [0.1] - 2016-06-09

Initial release

[Unreleased]: https://github.com/escaped/django-inline-actions/compare/2.4.0...HEAD
[2.4.0]: https://github.com/escaped/django-inline-actions/compare/2.3.0...2.4.0
[2.3.0]: https://github.com/escaped/django-inline-actions/compare/2.2.0...2.3.0
[2.2.0]: https://github.com/escaped/django-inline-actions/compare/2.1.0...2.2.0
[2.1.0]: https://github.com/escaped/django-inline-actions/compare/2.0.2...2.1.0
[2.0.2]: https://github.com/escaped/django-inline-actions/compare/2.0.2...2.1.0
[2.0.1]: https://github.com/escaped/django-inline-actions/compare/2.0.0...2.0.1
[2.0.0]: https://github.com/escaped/django-inline-actions/compare/1.2.0...2.0.0
[1.2.0]: https://github.com/escaped/django-inline-actions/compare/1.1.0...1.2.0
[1.1.0]: https://github.com/escaped/django-inline-actions/compare/1.0.0...1.1.0
[1.0.0]: https://github.com/escaped/django-inline-actions/compare/0.1...1.0.0
[0.1]: https://github.com/escaped/django-inline-actions/tree/0.1